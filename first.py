class grid:
	def __init__(self, x, y, totalMaps):
		i = 0
		_maps = []
		while(i < totalMaps):
			i += 1
			map = [[0 for _x in range(x)] for _y in range(y)]
			_maps.append(map)
		self.maps = _maps


def init(preloadMap):
	myGrid = grid(4, 4, 1)
	if(preloadMap == 1):
		myGrid = grid(5, 5, 1)
		arr = myGrid.maps[0]
		arr[1][2] = 1
		arr[2][2] = 1
		arr[2][3] = 1
		arr[3][2] = 1
		arr[3][3] = 1
		arr[4][3] = 1
		myGrid.maps[0] = arr
		print(len(arr))
	arr = myGrid.maps[0]
	for _x in range(len(arr)):
		print(myGrid.maps[0][_x])

def main():
	print("hello, would you like to load the example")
	answer = int(input())
	#print(answer)
	if(answer == 1):
		init(1)
	else:
		init(0)

if __name__ == "__main__":
	main()
