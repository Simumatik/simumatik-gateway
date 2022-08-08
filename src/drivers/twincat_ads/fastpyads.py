import pyads
from typing import Any, Dict, List, Optional
import struct
import time

from pyads.pyads_ex import (
    adsSyncReadWriteReqEx2,
)
from pyads.structs import (
    SAdsSumRequest,
)
from pyads.constants import (
    DATATYPE_MAP,
    ADSIGRP_SUMUP_READ,
    ADSIGRP_SUMUP_WRITE,
    ads_type_to_ctype,
)
from pyads.errorcodes import ERROR_CODES


class fastConnection (pyads.Connection):

    def read_list_by_name(
            self,
            data_names: List[str]
    ) -> Dict[str, Any]:

        result: Dict[str, Optional[Any]] = {i: None for i in data_names}

        num_requests = len(data_names)

        sum_req_array_type = SAdsSumRequest * num_requests
        sum_req_array = sum_req_array_type()

        for i, data_name in enumerate(data_names):
            sum_req_array[i].iGroup = self._symbol_info_cache[data_name].iGroup
            sum_req_array[i].iOffset = self._symbol_info_cache[data_name].iOffs
            sum_req_array[i].size = self._symbol_info_cache[data_name].size

        t = time.perf_counter()
        sum_response = adsSyncReadWriteReqEx2(
            self._port, 
            self._adr,
            ADSIGRP_SUMUP_READ,
            num_requests,
            None,
            sum_req_array,
            None,
            return_ctypes=False,
            check_length=False,
        )
        delta = time.perf_counter()-t
        if delta>0.010:
            print(f'{time.perf_counter()}:{len(data_names)} variables read in {delta}s')

        data_start = 4 * num_requests
        offset = data_start

        for i, data_name in enumerate(data_names):
            error = struct.unpack_from("<I", sum_response, offset=i * 4)[0]
            if error:
                result[data_name] = ERROR_CODES[error]
            else:
                value = struct.unpack_from(
                    DATATYPE_MAP[ads_type_to_ctype[self._symbol_info_cache[data_name].dataType]],
                    sum_response,
                    offset=offset,
                )[0]
                result[data_name] = value  
            offset += self._symbol_info_cache[data_name].size

        return result


    def write_list_by_name(
            self,
            data_names_and_values: Dict[str, Any]
    ):
        offset = 0
        num_requests = len(data_names_and_values)
        total_request_size = num_requests * 3 * 4  # iGroup, iOffset & size

        for data_name in data_names_and_values.keys():
            total_request_size += self._symbol_info_cache[data_name].size

        buf = bytearray(total_request_size)

        for data_name in data_names_and_values.keys():
            struct.pack_into("<I", buf, offset, self._symbol_info_cache[data_name].iGroup)
            struct.pack_into("<I", buf, offset + 4, self._symbol_info_cache[data_name].iOffs)
            struct.pack_into("<I", buf, offset + 8, self._symbol_info_cache[data_name].size)
            offset += 12

        for data_name, value in data_names_and_values.items():
            struct.pack_into(
                DATATYPE_MAP[ads_type_to_ctype[self._symbol_info_cache[data_name].dataType]],
                buf,
                offset,
                value,
            )
            offset += self._symbol_info_cache[data_name].size

        t = time.perf_counter()
        adsSyncReadWriteReqEx2(
            self._port, 
            self._adr,
            ADSIGRP_SUMUP_WRITE,
            num_requests,
            None,
            buf,
            None,
            return_ctypes=False,
            check_length=False,
        )
        delta = time.perf_counter()-t
        if delta>0.010:
            print(f'{time.perf_counter()}:{len(data_names_and_values)} variables written in {delta}s')