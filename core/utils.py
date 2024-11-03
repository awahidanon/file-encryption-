from .models import ActionLog

def track_action(user, file, action, info=None):
    """
    Creates an action log entry.

    Parameters:
        user (User): The user performing the action.
        file (FileEncryption): The file on which the action is performed.
        action (str): The action performed ('upload', 'download', 'share', 'view').
        info (str, optional): Additional information related to the action.
    """
    ActionLog.objects.create(user=user, file=file, action=action, additional_info=info)
