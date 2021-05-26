from httpAuto.models.case_log import CaseLog


def Log(result_id, level, msg):
    CaseLog.objects.create(result_id, level, msg)
