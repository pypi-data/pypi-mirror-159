import maya
from hypothesis.strategies import datetimes

def maya_dts(*args, **kwargs):
	return datetimes(*args, **kwargs).map(maya.MayaDT.from_datetime)