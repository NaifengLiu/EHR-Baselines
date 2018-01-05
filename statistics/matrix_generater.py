import numpy as np
from datetime import datetime

print str(datetime.now()) + "   1"
previous_person_matrix = np.zeros((4019, 2038))
print str(datetime.now()) + "   2"
np.savetxt("text", previous_person_matrix)
print str(datetime.now()) + "   3"
