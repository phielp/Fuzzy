# run command in matlab to start connection
# matlab.engine.shareEngine

import matlab.engine
engine = matlab.engine.connect_matlab()

result = engine.FLS(5.0, 0.5)
print(result)


	


# engine.quit()