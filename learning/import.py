import sys
MODULE = r"F:\MayaTecent\UnrealScript\learning"
if MODULE not in sys.path:
    sys.path.append(MODULE)

import unrealTest
reload(unrealTest)

