import pytest

def user_payload(
    equipment_id = "999",
    student_id = "ST-AB1234",
    description = "student equipment maintenance",
    priority = "2"
):
    return {
        "equipment_id": equipment_id,
        "student_id": student_id,
        "description": description,
        "priority": priority,
    }





    

