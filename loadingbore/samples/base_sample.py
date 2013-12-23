from loadingbore.bore import BoreBase
import time

b = BoreBase()

b.draw()
for progress in xrange(100):
    time.sleep(0.05)
    b.update(progress + 1).draw()
