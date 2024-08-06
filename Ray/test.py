import ray
import time


class RayTest :

    def __init__(self) :
        ray.init(num_cpus=2)
        pass
    
    @staticmethod
    @ray.remote
    def add(x,y) :
        return x+y
    
    def run(self) :
        values = [(1,2),(3,4),(4,5),(5,6)]
        results = [self.add.remote(x,y) for x,y in values]
        results = ray.get(results)
        print(results)

def test1() :
    t = RayTest()
    t.run()


@ray.remote
class RayTestActor :

    def add(self,x,y) :
        return x+y
    
def test2() :
    ray.init(num_cpus=2)
    ray_test_actor = RayTestActor.remote()

    values = [(1, 2), (3, 4), (4, 5), (5, 6)]
    results = [ray_test_actor.add.remote(x, y) for x, y in values]
    #print(results) ray Object
    results = ray.get(results)
    print(results)
    
test2()

 