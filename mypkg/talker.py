import rclpy                #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query   #通信の型（16ビットの符号付き整数）

rclpy.init() 
node = Node("talker")           #ノード作成（nodeという「オブジェクト」を作成）

def cb(request, response):          
    if request.name == "平地健太":
        response.age = 22
    else:
        response.age = 255

    return response


def main():
    srv = node.create_service(Query,"query", cb)  
    rclpy.spin(node)            
