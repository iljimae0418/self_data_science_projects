import numpy as np 
k = 4 
num_val_samples = len(train_data)//k 
num_epochs = 100 
all_scores = [] 
for i in range(k):  
  print("currently at fold {}".format(i)) 
  val_data = train_data[i * num_val_samples: (i+1) * num_val_samples]   
  val_targets = train_targets[i * num_val_samples:(i+1) * num_val_samples] 
  
  partial_train_data = np.concatenate([train_data[:i * num_val_samples], train_data[(i+1) * num_val_samples:]],axis=0) 
  partial_train_targets = np.concatenate([train_targets[:i * num_val_samples], train_targets[(i+1) * num_val_samples:]],axis=0) 
  
  model = build_model() 
  model.fit(partial_train_data, partial_train_targets, epochs = num_epochs, batch_size = 1, verbose = 1) 
  val_mse, val_mae = model.evaluate(val_data, val_targets, verbose = 1)
  all_scores.append(val_mae) 

print(np.mean(all_scores))
