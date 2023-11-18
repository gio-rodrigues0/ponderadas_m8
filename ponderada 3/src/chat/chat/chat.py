import re
import rclpy
from rclpy.node import Node

class Chat(Node):

    def __init__(self):
        super().__init__('chat')
        
        self.intent_dict = {
            r"\b(?:(?:(?:[Mm]e [Ll]ev[ea])|(?:[Vv][áa]))?\s?(?:(?:[Pp]ara [oa])|(?:[Aa]t[ée] [oa]))?\s?(?:[Ll]aboratório|[Ll]aboratorio|[Ll]ab|[Ll]abo))": 'lab',
            r"\b(?:(?:(?:[Mm]e [Ll]ev[ea])|(?:[Vv][áa]))?\s?(?:(?:[Pp]ara [oa])|(?:[Aa]t[ée] [oa]))?\s?(?:[Cc]entral|[Gg]rêmio|[Gg]remio))": 'central',
            r"\b(?:(?:(?:[Mm]e [Ll]ev[ea])|(?:[Vv][áa]))?\s?(?:(?:[Pp]ara [oa])|(?:[Aa]t[ée] [oa]))?\s?(?:[Ss]ala|[Aa]teliê|[Aa]telie))": 'sala',
            r"(?:[Ss]air|[Ee]ncerrar|[Ee]xit)": 'sair'
        }

        self.action_dict = {
            'lab': self.lab,
            'central': self.central,
            'sala': self.sala,
            'sair': self.sair
        }

    def lab(self, _):
        self.get_logger().info('Going to lab')

    def central(self, _):
        self.get_logger().info('Going to central')

    def sala(self, _):
        self.get_logger().info('Going to sala')

    def sair(self, _):
        self.get_logger().info('Exiting')
        rclpy.shutdown()
        exit()

    def running(self):
        while rclpy.ok():
            command = input('Enter command: ')
            for key, value in self.intent_dict.items():
                pattern = re.compile(key)
                groups = pattern.findall(command)
                if groups:
                    self.action_dict[value](groups[0])
                    break 
            else:
                self.get_logger().info('Invalid command')
                
def main():
    rclpy.init()
    chat = Chat()
    chat.running()
    rclpy.spin(chat)
    chat.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()