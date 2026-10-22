import sys
import sysconfig
import shutil
import subprocess
import asyncio
import shutil
from pathlib import Path
from os import getenv
from importlib.util import find_spec
from simumatik_api_helper import UploadFile, GetRequestJson, GetSimumatikApiToken

''' 
    note-signtool:
    Follow this guide: https://learn.microsoft.com/en-us/azure/artifact-signing/how-to-signing-integrations#set-up-signtool-to-use-artifact-signing

    Requirements

    -   You have to use a domain connected computer.

    -   Your Azure account has to have the "Artifact Signing Certificate Profile Signer" role.
        Before calling this script you need to login using the Azure CLI with the command "az login". On a company computer it should bring up
        a prompt to authorize the action using your Microsoft account. If you did not get a prompt the browser may open a login prompt, but
        that seems to be restricted even if you successfully log in.

    -   You have to create a metadata.json in the project root directory (i.e this directory) with the values you got from your admin:

            {
                "Endpoint": "<replace this>",
                "CodeSigningAccountName": "<replace this>",
                "CertificateProfileName": "<replace this>",
                "CorrelationId": "<replace this>"
            }

        Do _NOT_ commit metadata.json.

    -   If you used the Artifact Signing Client Tools Installer the Azure.CodeSigning.Dlib.dll is assumed to be located in %LOCALAPPDATA%/Microsoft/MicrosoftArtifactSigningClientTools/Azure.CodeSigning.Dlib.dll.
        Otherwise you _have_ to supply the path to the Azure.CodeSigning.Dlib.dll when calling this script (see the guide above):

        deploy_package.py <path to Azure.CodeSigning.Dlib.dll>

    If you want to call SignTool to sign manually the following command is used:
        C:/"Program Files (x86)"/"Windows Kits"/10/bin/10.0.26100.0/x64/signtool.exe sign /v /debug /fd SHA256 /tr "http://timestamp.acs.microsoft.com" /td SHA256 /dlib "<path to Azure.CodeSigning.Dlib.dll>" /dmdf "metadata.json" dist/workspace/LocalWorkspace.exe
'''

PLATFORM = sys.platform
print("Platform:", PLATFORM)
OS_EXECUTABLE_EXT = {"win32": "exe", "linux": "sh", "darwin": "sh"}

PYTHON_EXECUTABLE = Path(sys.executable);
print("Python executable:", PYTHON_EXECUTABLE)

PYTHON_SCRIPTS_PATH = Path(sysconfig.get_path("scripts"))
assert PYTHON_SCRIPTS_PATH.exists(), "Could not find the Python scripts directory."

PYTHON_VERSION_INFO = sys.version_info
print(f"Python version: {PYTHON_VERSION_INFO.major}.{PYTHON_VERSION_INFO.minor}.{PYTHON_VERSION_INFO.micro}")

# Make sure the Python version of the current interpreter is 3.14.x.
assert PYTHON_VERSION_INFO >= (3, 14) and PYTHON_VERSION_INFO < (3, 15), "deploy_package.py requires Python 3.14.x"

# For relative references
REPOSITORY_PATH=Path(__file__).parent
print ("Repository:",  REPOSITORY_PATH)

PACKAGE = 'gateway'
PACKAGE_EXECUTABLE = f'{PACKAGE}.{OS_EXECUTABLE_EXT[PLATFORM]}'

print("Executable name:", PACKAGE_EXECUTABLE)

print(f"Deploying {PACKAGE} package for platform {PLATFORM}...")

# WINDOWS
if PLATFORM=="win32":
    dlibPath = Path(f"{getenv('LOCALAPPDATA')}/Microsoft/MicrosoftArtifactSigningClientTools/Azure.CodeSigning.Dlib.dll")
    if len(sys.argv) >= 2:
        print(f"Using path to Azure.CodeSigning.Dlib.dll from command line (\"{sys.argv[1]}\")")
        dlibPath = Path(sys.argv[1])
    else:
        print(f"Trying to find Azure.CodeSigning.Dlib.dll in the Artifact Signing Client Tools Installer install path ({dlibPath})")

    assert dlibPath.exists() and dlibPath.is_file(), "Could not find the Azure.CodeSigning.Dlib.dll"

    PACKAGE_DIST =  f'dist/{PACKAGE}'
    OUTPUT_DIRECTORY = REPOSITORY_PATH / PACKAGE_DIST
    SPEC_FILE = f'{PACKAGE}_package.spec'

    PYINSTALLER_COMMAND = [PYTHON_EXECUTABLE, "-m", "PyInstaller", "--noconfirm", REPOSITORY_PATH / SPEC_FILE]
    pyInstallerSpec = find_spec("PyInstaller")
    assert pyInstallerSpec is not None, "⚠️  Could not find the PyInstaller module. Did you install the requirements?"

    SIGNTOOLS_PATH = Path("C:/Program Files (x86)/Windows Kits/10/bin/10.0.26100.0/x64/signtool.exe")
    assert SIGNTOOLS_PATH.exists(), "⚠️  Could not find signtool.exe"

    ARTIFACT_SIGNING_DLIB_PATH = dlibPath

    EXECUTABLE_PATH = f"{OUTPUT_DIRECTORY}/{PACKAGE_EXECUTABLE}"

    SIGNTOOLS_CODE_SIGNING_COMMAND = [
          SIGNTOOLS_PATH,
          "sign",
          "/v",
          "/debug",
          "/fd", "SHA256",
          "/tr", "http://timestamp.acs.microsoft.com",
          "/td", "SHA256",
          "/dlib", ARTIFACT_SIGNING_DLIB_PATH,
          "/dmdf", REPOSITORY_PATH/"metadata.json",
          EXECUTABLE_PATH
    ];

    if subprocess.call(PYINSTALLER_COMMAND, shell=True) != 0:
        raise RuntimeError("Something went wrong with the PyInstaller command. Deploy aborted.")
    if subprocess.call(SIGNTOOLS_CODE_SIGNING_COMMAND, shell=True) != 0:
        raise RuntimeError("Something went wrong with the SignTool code signing command. Deploy aborted.")


# LINUX
elif PLATFORM=="linux":
    pass
# MACOS
elif PLATFORM=="darwin":
    pass

TOKEN, AUDIENCE = GetSimumatikApiToken()
assert TOKEN is not None, "Error getting Simumatik API token!"

print("[+] Do you want to deploy a regular (Default) or experimental (1) package?")
experimental = input() == '1'

# TODO: Fix new paths for other platforms
if experimental:
    actual_version = asyncio.run(GetRequestJson(token=TOKEN, url=f'{AUDIENCE}/{PACKAGE}/experimental/version'))
else:
    actual_version = asyncio.run(GetRequestJson(token=TOKEN, url=f'{AUDIENCE}/{PACKAGE}/version'))

print(f"Actual {PACKAGE} package version is: {actual_version}")
print("[+] Introduce the new version number (i.e. '1.0.0'): ")
version = input()
filepath = 'Output/'

print("Zipping the package...")
shutil.make_archive(f'{filepath}{PACKAGE}-{version}', 'zip', f'dist/{PACKAGE}')
filename = f'{PACKAGE}-{version}.zip'

print('Uploading package...')
if experimental:
    asyncio.run(UploadFile(token=TOKEN, url=f'{AUDIENCE}/admin/{PACKAGE}/experimental', path=filepath, filename=filename))
else:
    asyncio.run(UploadFile(token=TOKEN, url=f'{AUDIENCE}/admin/{PACKAGE}', path=filepath, filename=filename))

print('Package uploaded!')
if experimental:
    version = asyncio.run(GetRequestJson(token=TOKEN, url=f'{AUDIENCE}/{PACKAGE}/experimental/version'))
else:
    version = asyncio.run(GetRequestJson(token=TOKEN, url=f'{AUDIENCE}/{PACKAGE}/version'))

print(f"Uploaded {PACKAGE} package version is: {version}")