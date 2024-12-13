import rclpy                #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.msg import Query   #通信の型（16ビットの符号付き整数）

rclpy.init() 
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0

def cb():
    global n
    msg = Person()
    msg.name = "Kenta Hirachi"
    msg.age = n
    pub.publish(msg)
    n += 1

def main():
    srv = node.create_service(Query, "query", cb)
    rclpy.spin(node)            #実行（無限ループ）
