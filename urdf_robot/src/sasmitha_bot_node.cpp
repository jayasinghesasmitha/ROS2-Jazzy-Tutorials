#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include <random>

class SasmithaBotNode : public rclcpp::Node {
public:
    SasmithaBotNode() : Node("sasmitha_bot_node") {
        pub_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel", 10);
        sub_ = this->create_subscription<sensor_msgs::msg::LaserScan>("/scan", 10,
            std::bind(&SasmithaBotNode::scan_callback, this, std::placeholders::_1));
        timer_ = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&SasmithaBotNode::move_random, this));
    }

private:
    void scan_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg) {
        obstacle_ = false;
        for (float range : msg->ranges) {
            if (range < 0.5) {
                obstacle_ = true;
                break;
            }
        }
    }

    void move_random() {
        geometry_msgs::msg::Twist twist;
        if (obstacle_) {
            twist.angular.z = random_sign() * 0.8;
        } else {
            twist.linear.x = 0.2;
        }
        pub_->publish(twist);
    }

    int random_sign() {
        return (rand() % 2 == 0) ? 1 : -1;
    }

    bool obstacle_ = false;
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub_;
    rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr sub_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[]) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<SasmithaBotNode>());
    rclcpp::shutdown();
    return 0;
}