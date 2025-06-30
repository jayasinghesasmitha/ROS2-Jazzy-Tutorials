Here is a complete README.md file with step-by-step instructions for running all 6 tasks in your ROS 2 Jazzy workspace, including special notes and common pitfalls.

📄 README.md

# ROS 2 Tasks (Jazzy) – Instructions

This repository contains 6 custom ROS 2 nodes and one launch file. Follow the steps below to build and test each task individually.

---

## ✅ Prerequisites

* ROS 2 Jazzy installed
* Colcon workspace: \~/ros2\_ws
* Source ROS environment:

  ```bash
  source /opt/ros/jazzy/setup.bash
  ```

---

## 🛠️ 1. Workspace Setup

1. Create the workspace if not already done:

   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   ```

2. Clone or place your packages:

   * ros2\_tasks (contains task nodes + launch file)
   * tests (contains chatter and listener)

3. Build and source:

   ```bash
   cd ~/ros2_ws
   colcon build
   source install/setup.bash
   ```

---

## 🚀 Task 1: pose\_re\_pub

📌 Description:
Subscribes to /pose\_with\_covariance\_stamped and republishes pose to /pose.

📦 Run:

```bash
ros2 run ros2_tasks pose_re_pub
```

📋 Test:
In another terminal:

```bash
ros2 topic pub /pose_with_covariance_stamped geometry_msgs/PoseWithCovarianceStamped \
  '{pose: {pose: {position: {x: 1.1, y: 2.2, z: 3.3}, orientation: {x: 0.1, y: 0.2, z: 0.3, w: 0.4}}}}'
```

Check:

```bash
ros2 topic echo /pose
```

✅ You should see matching position and orientation.

---

## 🚀 Task 2: params\_setter

📌 Description:
Sets a ROS parameter globally on node startup.

📦 Run:

```bash
ros2 run ros2_tasks params_setter
```

📋 Test:
In a second terminal:

```bash
ros2 param list
ros2 param get /params_setter example_param
```

✅ You should see example\_param: hello\_ros

🔎 Note:
This node must stay running (uses rclpy.spin()) for parameter to remain available.

---

## 🚀 Task 3: twist\_from\_database

📌 Description:
Reads values.csv line-by-line and publishes Twist messages to /twist\_from\_database at 10 Hz.

📂 Make sure:
Place values.csv in: ros2\_tasks/ros2\_tasks/data/values.csv

📦 Run:

```bash
ros2 run ros2_tasks twist_from_database
```

📋 Test:

```bash
ros2 topic echo /twist_from_database
```

✅ You should see Twist messages corresponding to CSV values.

📌 Special Note:
File is accessed using importlib.resources — it must be correctly installed using setup.py package\_data.

---

## 🚀 Task 4: zero\_twist

📌 Description:
Subscribes to /is\_stopped (std\_msgs/String) and publishes zero Twist message to /twist when "true".

📦 Run:

```bash
ros2 run ros2_tasks zero_twist
```

📋 Test:
In another terminal:

```bash
ros2 topic pub /is_stopped std_msgs/String "data: 'true'"
```

Check:

```bash
ros2 topic echo /twist
```

✅ Should publish a Twist with all zeros once "true" is received.

❌ Does not publish if message is "false" or topic is silent.

---

## 🚀 Task 5: test\_launch.py

📌 Description:
Launches:

* tests/chatter → /test/chatter (renamed)
* tests/listener
* Publishes one zero Twist message to /twist

📦 Run:

```bash
ros2 launch ros2_tasks test_launch.py
```

📋 Test:

```bash
ros2 topic echo /test/chatter
ros2 topic echo /twist
```

✅ You should see chatter messages and a one-time Twist publish.

⚠️ Special Notes:

* Your tests package must exist with chatter.py and listener.py as console\_scripts.
* The launch file uses bash -c to safely wrap ros2 topic pub.

---

## 🚀 Task 6: param\_reader

📌 Description:
Reads parameter /robot\_name and prints it on startup.

📦 Run:

```bash
ros2 run ros2_tasks param_reader --ros-args -p robot_name:=CryoBot
```

✅ Output in terminal:
Robot name: CryoBot

---

## 💡 Common Errors & Fixes

| Error Message                          | Cause                                | Fix                                                    |
| -------------------------------------- | ------------------------------------ | ------------------------------------------------------ |
| FileNotFoundError: values.csv          | File not installed properly          | Place it inside ros2\_tasks/data/ and update setup.py  |
| ros2: error: unrecognized arguments... | Improper Twist syntax in launch file | Use bash -c in ExecuteProcess with correct YAML syntax |
| No output from param list              | Node exited too soon                 | Use rclpy.spin() to keep node alive                    |
| Launch file not found                  | Not installed in setup.py            | Add launch/ to data\_files in setup.py                 |

---

Let me know if you'd like this formatted and saved as an actual file in your repo!
