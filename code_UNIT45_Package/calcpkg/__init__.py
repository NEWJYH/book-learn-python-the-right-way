# from . import operation # 현재 패키지에서 operation 모듈을 가져옴
# from . import geometry # 현재 패키지에서 geometry 모듈을 가져옴


'''패키지 독스트링'''

# __init__.py  수정 
# from .operation import add, mul 
# from .geometry import triangle_area, rectangle_area

# # __init__.py  수정2
# from .operation import * 
# from .geometry import *

# # 필요한 것만 공개하기
# __all__ = ['add','triangle_area'] # calcpkg패키지에서 add, triangle_area 함수만 공개

# from .operation.operation import *
# from .geometry.geometry import *

from .operation.element import *
from .operation.logic import *
from .geometry.shape import *
from .geometry.vector import *