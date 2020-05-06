def smooth_curve(points, factor = 0.9): 
  smoothed_points = [] 
  for point in points: 
    if smooted_points: 
      previous = smooted_points[-1] 
      smooted_points.append(previous * factor + point * (1-factor))  
    else:  
      smootehd_points.append(point) 
  return smooted_points 
