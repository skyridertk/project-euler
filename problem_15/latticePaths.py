def latticePaths(gridSize):
  vertices = []
  terminating_vertices = []
  path = 0

  for i in range(gridSize+1):
    vertices.append([0, i])
    terminating_vertices.append([i, 0])

  for j in range(1, gridSize+1):
    vertices.append([j, vertices[len(vertices)-1][1]])
    terminating_vertices.append([vertices[len(vertices)-1][1], j])

  path += 2

  '''
  break_point = False
  stages = 0
  while not break_point:
    for val in range(len(vertices)):
      if(vertices[val][0] == 1 and vertices[val+1][0] == 2):
        print(vertices[val])
      

      if(vertices[val][0] == 2):
        break
    

      #if #20 is reached break point True
    
    if(break_point == False):
      stages += 1
  '''
  print(vertices)
  print(terminating_vertices)
  #00
  #01
  #02 x
  #12
  #22

  #00
  #01
  #11
  #12 x
  #22

  #Repeat
  #00
  #01 y
  #11
  #21
  #22

  #00
  #10
  #11
  #12
  #22

  #00
  #10
  #11
  #21
  #22

  #00
  #10
  #20
  #21
  #22
  return True


print(latticePaths(3))