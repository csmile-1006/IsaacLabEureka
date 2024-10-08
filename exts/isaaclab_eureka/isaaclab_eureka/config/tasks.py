# Copyright (c) 2024, The Isaac Lab Project Developers.
#
# SPDX-License-Identifier: Apache-2.0

TASKS_CFG = {
    "Isaac-Cartpole-Direct-v0": {
        "description": "balance a pole on a cart so that the pole stays upright",
        "success_metric": "self.episode_length_buf[env_ids].float().mean() / self.max_episode_length",
        "success_metric_to_win": 1.0,
        "success_metric_tolerance": 0.01,
    },
    "Isaac-Quadcopter-Direct-v0": {
        "description": (
            "bring the quadcopter to the target position: self._desired_pos_w, while making sure it flies smoothly"
        ),
        "success_metric": (
            "torch.linalg.norm(self._desired_pos_w[env_ids] - self._robot.data.root_pos_w[env_ids], dim=1).mean()"
        ),
        "success_metric_to_win": 0.0,
        "success_metric_tolerance": 0.2,
    },
    "Isaac-Franka-Cabinet-Direct-v0": {
        "description": "grasp the handle of a cabinet’s drawer and open it with the Franka robot",
        "success_metric": "self._cabinet.data.joint_pos[:, 3] > 0.39",
        "success_metric_to_win": 1.0,
        "success_metric_tolerance": 0.01,
    },
    "Isaac-GR1T2-Jaw-Upper-Organize-Direct-v0": {
        "description": (
            "Using the arm closest to the cup, grasp the messy cup on the desk and place it back in an upright"
            " position."
        ),
        "success_metric": (
            "torch.logical_and(abs(rotation_distance(self.object.data.root_quat_w, self.goal_rot)) <"
            " self.cfg.object_upright_threshold, self.object.data.root_pos_w[:, 2] <= self.cfg.table_height +"
            " self.cfg.epsilon)"
        ),
        "success_metric_to_win": 1.0,
        "success_metric_tolerance": 0.01,
    },
    "Isaac-GR1T2-Jaw-Upper-Organize-Unimanual-Vision-Direct-v0": {
        "description": (
            "Using the arm closest to the cup, grasp the messy cup on the desk and place it back in an upright"
            " position."
        ),
        "success_metric": (
            "torch.logical_and(abs(rotation_distance(self.object.data.root_quat_w, self.goal_rot)) <"
            " self.cfg.object_upright_threshold, self.object.data.root_pos_w[:, 2] <= self.cfg.table_height +"
            " self.cfg.epsilon)"
        ),
        "success_metric_to_win": 1.0,
        "success_metric_tolerance": 0.01,
    },
    "Isaac-GR1T2-Jaw-Upper-Organize-Bimanual-Vision-Direct-v0": {
        "description": (
            "Using the arm closest to the cup, grasp the messy cup on the desk and place it back in an upright"
            " position."
        ),
        "success_metric": (
            "torch.logical_and(abs(rotation_distance(self.object.data.root_quat_w, self.goal_rot)) <"
            " self.cfg.object_upright_threshold, self.object.data.root_pos_w[:, 2] <= self.cfg.table_height +"
            " self.cfg.epsilon)"
        ),
        "success_metric_to_win": 1.0,
        "success_metric_tolerance": 0.01,
    },
    "Isaac-GR1T2-Legato-Upper-Organize-Unimanual-Vision-Direct-v0": {
        "description": (
            "Using the arm closest to the cup, grasp the messy cup on the desk and place it back in an upright"
            " position."
        ),
        "success_metric": (
            "torch.logical_and(abs(rotation_distance(self.object.data.root_quat_w, self.goal_rot)) <"
            " self.cfg.object_upright_threshold, self.object.data.root_pos_w[:, 2] <= self.cfg.table_height +"
            " self.cfg.epsilon)"
        ),
        "success_metric_to_win": 1.0,
        "success_metric_tolerance": 0.01,
    },
    "Isaac-GR1T2-Legato-Upper-Organize-Bimanual-Vision-Direct-v0": {
        "description": (
            "Using the arm closest to the cup, grasp the messy cup on the desk and place it back in an upright"
            " position."
        ),
        "success_metric": (
            "torch.logical_and(abs(rotation_distance(self.object.data.root_quat_w, self.goal_rot)) <"
            " self.cfg.object_upright_threshold, self.object.data.root_pos_w[:, 2] <= self.cfg.table_height +"
            " self.cfg.epsilon)"
        ),
        "success_metric_to_win": 1.0,
        "success_metric_tolerance": 0.01,
    },
}
"""Configuration for the tasks supported by Isaac Lab Eureka.

`TASKS_CFG` is a dictionary that maps task names to their configuration. Each task configuration
is a dictionary that contains the following keys:

- `description`: A description of the task.
- `success_metric`: A Python expression that computes the success metric for the task.
- `success_metric_to_win`: The threshold for the success metric to win the task and stop.
- `success_metric_tolerance`: The tolerance for the success metric to consider the task successful.
"""
