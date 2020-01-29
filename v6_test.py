board_file_2020 = {
    "year": 2020,
    "revision": 2,
    "robot_scout": {
        "screens": [
            {
                "title": "Auto",
                "layout": [
                    [
                        {
                            "name": "trench_intake",
                            "type": "Button",
                            "options": []
                        },
                        {
                            "name": "fed",
                            "type": "Button",
                            "options": []
                        },
                        {
                            "name": "other_intake",
                            "type": "Button",
                            "options": []
                        }
                    ],
                    [
                        {
                            "name": "low",
                            "type": "Button",
                            "options": []
                        },
                        {
                            "name": "inner",
                            "type": "Button",
                            "options": []
                        },
                        {
                            "name": "outer",
                            "type": "Button",
                            "options": []
                        }
                    ],
                    [
                        {
                            "name": "low_miss",
                            "type": "Button",
                            "options": []
                        },
                        {
                            "name": "high_miss",
                            "type": "Button",
                            "options": []
                        }
                    ],
                    [
                        {
                            "name": "field_area",
                            "type": "MultiToggle",
                            "options": [
                                "Cross",
                                "Mid",
                                "Init",
                                "Target"
                            ]
                        }
                    ]
                ]
            },
            {
                "title": "Teleop",
                "layout": [
                    [
                        {
                            "name": "control_panel",
                            "type": "Switch",
                            "options": []
                        },
                        {
                            "name": "defending",
                            "type": "Switch",
                            "options": []
                        },
                        {
                            "name": "resisting",
                            "type": "Switch",
                            "options": []
                        }
                    ],
                    [
                        {
                            "name": "low",
                            "type": "Button",
                            "options": []
                        },
                        {
                            "name": "inner",
                            "type": "Button",
                            "options": []
                        },
                        {
                            "name": "outer",
                            "type": "Button",
                            "options": []
                        }
                    ],
                    [
                        {
                            "name": "low_miss",
                            "type": "Button",
                            "options": []
                        },
                        {
                            "name": "high_miss",
                            "type": "Button",
                            "options": []
                        }
                    ],
                    [
                        {
                            "name": "field_area",
                            "type": "MultiToggle",
                            "options": [
                                "Cross",
                                "Mid",
                                "Init",
                                "Target"
                            ]
                        }
                    ]
                ]
            },
            {
                "title": "Endgame",
                "layout": [
                    [
                        {
                            "name": "climb",
                            "type": "MultiToggle",
                            "options": [
                                "None",
                                "Attempt",
                                "Success"
                            ]
                        }
                    ],
                    [
                        {
                            "name": "climb_location",
                            "type": "MultiToggle",
                            "options": [
                                "Middle",
                                "Up",
                                "Down",
                                "Balanced"
                            ]
                        }
                    ],
                    [
                        {
                            "name": "balanced_after_climb",
                            "type": "Checkbox",
                            "options": []
                        }
                    ],
                    [
                        {
                            "name": "active_movement",
                            "type": "Checkbox",
                            "options": []
                        }
                    ]
                ]
            }
        ],
        "tags": []
    },
    "super_scout": {
        "screens": [],
        "tags": []
    }
}


enc = "2019marcm_4:4130:Unknown_Scout:R1:5e30a3e0:KABlLABlHEBlEEEwCEEwBEEwGEEwHEEwHEwuGEwuDEyTJEyTFEyTIEz3JAz3GE4kLE4kKE6I:"

from v6 import *

bf = Boardfile(board_file_2020)
print(bf.robot_scout.lookup("auto", "field_area"))
print(parse_entry(enc))

# print(parse_entry(enc))