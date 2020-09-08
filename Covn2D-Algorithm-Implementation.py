def conv2D(matrix, kernal, step=1):
  er, ec = kernal.shape[0], kernal.shape[0]
  convd = []
  for sr in range(matrix.shape[0]-(kernal.shape[0]-1)):
      for sc in range(matrix.shape[0]-(kernal.shape[0]-1)):
        temp = matrix[sr:er, sc:ec] * kernal
        convd.append(np.amax(temp))
        ec += step
        if (sc == (matrix.shape[0] - (kernal.shape[0] - 1) - 1)): 
          ec = kernal.shape[0]
          er += step

  return np.array(convd).reshape(matrix.shape[0]-(kernal.shape[0]-1), matrix.shape[0]-(kernal.shape[0]-1))
