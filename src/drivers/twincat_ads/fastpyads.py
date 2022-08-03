import pyads
from typing import Any, Dict, List, Optional
import struct

from pyads.pyads_ex import (
    adsSyncReadWriteReqEx2,
)
from pyads.structs import (
    SAdsSumRequest,
)
from pyads.constants import (
    DATATYPE_MAP,
    ADSIGRP_SUMUP_READ,
    ads_type_to_ctype,
)
from pyads.errorcodes import ERROR_CODES


class fastpyads (pyads.Connection):

    def read_list_by_name(
            self,
            data_names: List[str]
    ) -> Dict[str, Any]:

        result: Dict[str, Optional[Any]] = {i: None for i in data_names}

        num_requests = len(data_names)

        # When a read is split, `data_symbols` will be bigger than `data_names`
        # Therefore we avoid looping over `data_symbols`

        sum_req_array_type = SAdsSumRequest * num_requests
        sum_req_array = sum_req_array_type()

        for i, name in enumerate(data_names):
            sum_req_array[i].iGroup = self._symbol_info_cache[name].iGroup
            sum_req_array[i].iOffset = self._symbol_info_cache[name].iOffs
            sum_req_array[i].size = self._symbol_info_cache[name].size

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
