from models.models import Profile
from conections.mysql import conection_userprofile

def edit_user(Id_User, Description=None, Id_preferences=None, Id_type=None):
    session = conection_userprofile()
    profile = session.query(Profile).filter_by(Id_User=Id_User, Status_account=1).first()

    if not profile:
        session.close()
        return {"error": "Active profile not found"}, 404

    if Description is not None:
        profile.Description = Description
    if Id_preferences is not None:
        profile.Id_preferences = Id_preferences
    if Id_type is not None:
        profile.Id_type = Id_type

    session.commit()
    session.close()
    return {"message": "Profile updated successfully"}, 200
