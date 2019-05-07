def jwt_response_payload_handeler(token,User=None,request=None):
    return{
        'token':token,
        'user':User.username
    }