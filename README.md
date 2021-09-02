[![Build Status](https://travis-ci.com/hashi0203/pimouse_run_corridor.svg?branch=main)](https://travis-ci.com/hashi0203/pimouse_run_corridor)

# pimouse_run_corridor

## 0. Prepare

If you haven't create catkin workspace, execute the following commands.

```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ source /opt/ros/melodic/setup.bash
$ catkin_init_workspace
$ cd ~/catkin_ws
$ catkin_make
```

## 1. Install

```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/hashi0203/pimouse_run_corridor.git
$ cd ~/catkin_ws
$ catkin_make
```

## 2. Run

- Terminal 1

    Start roscore.

    ```bash
    $ roscore
    ```

### 2.1. Wall Stop

Move a robot and stop it if it is close to a wall.

- Terminal 2

    ```bash
    $ roslaunch pimouse_run_corridor wall_stop.launch
    ```

### 2.2. Wall Stop Accel

Move and accelerate a robot and stop it if it is close to a wall.

- Terminal 2

    ```bash
    $ roslaunch pimouse_run_corridor wall_stop_accel.launch
    ```

### 2.3. Wall Trace

Trace a left wall and go straight if there is no wall.

- Terminal 2

    ```bash
    $ roslaunch pimouse_run_corridor wall_trace.launch
    ```

### 2.4. Wall Around

Trace a left wall and turn at corners.

- Terminal 2

    ```bash
    $ roslaunch pimouse_run_corridor wall_around.launch
    ```

## Reference

- 「[Raspberry Piで学ぶ ROSロボット入門](https://github.com/ryuichiueda/raspimouse_book_info)」