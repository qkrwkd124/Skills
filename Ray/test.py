import ray
import time
import logging
from logging.handlers import RotatingFileHandler


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

    def __init__(self):
        # 로그 설정
        self.logger = logging.getLogger("RayTestActor")
        self.logger.setLevel(logging.INFO)
        
        # RotatingFileHandler 설정
        handler = RotatingFileHandler(
            "./ray_test.log", maxBytes=5000, backupCount=3
        )
        handler.setLevel(logging.INFO)
        
        # 로그 포맷 설정
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # 핸들러를 로거에 추가
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def add(self,x,y) :
        return x+y
        
    def add2(self,x,y) :
        x,y = self.get_num(x,y)
        self.logger.info(f'log test {x}+{y}')
        print('gogo')
        time.sleep(5)
        return x+y
    
    def get_num(self,x,y) :
        return x+y, y-x
    
def test2() :
    ray.init(num_cpus=2)
    ray_test_actor = RayTestActor.remote()
    # ray_test_actor.add.remote(10,11)

    values = [(1, 2), (3, 4), (4, 5), (5, 6)]
    results = [ray_test_actor.add2.remote(x, y) for x, y in values]
    #print(results) ray Object
    results = ray.get(results)
    print(results)


@ray.remote
def add(x,y) :
    x,y = get_num(x,y)
    print(f'{x}+{y}')
    time.sleep(5)
    return x+y

def get_num(x,y) :
    print(x,y)
    return x+y, y-x

def test3() :
    ray.init(num_cpus=2)

    values = [(1, 2), (3, 4), (4, 5), (5, 6)]
    results = [add.remote(x, y) for x, y in values]
    results = ray.get(results)
    print(results)

test3()

 