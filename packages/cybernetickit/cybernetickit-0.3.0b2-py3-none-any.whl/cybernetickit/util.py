'''
Cybernetic Kit
Copyright (C) 2021  Civic Hacker, LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the Lesser GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
Lesser GNU General Public License for more details.

You should have received a copy of the Lesser GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import sys
import typing

if sys.version_info.major == 3 and sys.version_info.minor == 7:
    import typing_inspect
    def is_attr_required(atype) -> bool:
        return typing_inspect.get_origin(atype) is typing.Union and type(None) in typing_inspect.get_args(atype)
else:

    def is_attr_required(atype) -> bool:
        return typing.get_origin(atype) is typing.Union and type(None) in typing.get_args(atype)
