import numpy as np
from Alexnet import Alexnet

width = 80
height = 60
LR = 1e-3
epoch = 8
model_name = 'gta-autodrive.model'.fomat(LR, 'Alexnet2', epoch)

model = Alexnet(width, height, LR)

train_data = np.load('')

train = train_data[:-500]
x = np.array([i[0] for i in train]).reshape(-1, width, height, 1)
y = [i[1] for i in train]

test = train_data[-500:]
test_x = np.array([i[0] for i in test]).reshape(-1, width, height, 1)
test_y = [i[1] for i in test]

model.fit({'input': x},{'targets': y}, n_epochs=epoch,
			validation_set=({'input': test_x},{'targets': test_y}),
			snapshot_step=500, show_metric=True, run_id=model_name)

model.save(model_name)