import requests
import json
import time

LOGIN_URL = 'https://api.wrnch.ai/v1/login'
JOBS_URL = 'https://api.wrnch.ai/v1/jobs'

#Save the Cloud API key for next cell to work
API_KEY = ""

resp_auth = requests.post(LOGIN_URL,data={'api_key':API_KEY})
print(resp_auth.text)
# the jwt token is valid for an hour
JWT_TOKEN = json.loads(resp_auth.text)['access_token']

with open('Hi.jpg', 'rb') as f:
    resp_sub_job = requests.post(JOBS_URL,
                                 headers={'Authorization':f'Bearer {JWT_TOKEN}'},
                                 files={'media':f},
                                 data={'work_type':'json'}
                                )
    job_id = json.loads(resp_sub_job.text)['job_id']
    print('Status code:', resp_sub_job.status_code)
    print('Response:', resp_sub_job.text)

    time.sleep(3)

    GET_JOB_URL = JOBS_URL + '/' + job_id
    print(GET_JOB_URL)
    resp_get_job = requests.get(GET_JOB_URL, headers={'Authorization': f'Bearer {JWT_TOKEN}'})
    print('Status code:', resp_get_job.status_code)
    print('\nResponse:', resp_get_job.text)


    cloud_pose_estimation = json.loads(resp_get_job.text)

    cloud_xRELBOW = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][22]
    cloud_yRELBOW = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][23]
    cloud_xRWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][20]
    cloud_yRWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][21]

    cloud_xLELBOW = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][28]
    cloud_yLELBOW = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][29]
    cloud_xLWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][30]
    cloud_yLWRIST = cloud_pose_estimation['frames'][0]['persons'][0]['pose2d']['joints'][31]
"""""
    print(cloud_xLELBOW)
    print(cloud_yLELBOW)
    print(cloud_xLWRIST)
    print(cloud_yLWRIST)
    print("-------")


    print(cloud_xRELBOW)
    print(cloud_yRELBOW)
    print(cloud_xRWRIST)
    print(cloud_yRWRIST)
"""""

if cloud_yLWRIST >0 and cloud_yLELBOW >0 and cloud_yRELBOW >0 and cloud_yRWRIST >0:
    if  (cloud_yLELBOW > cloud_yLWRIST)and (cloud_yRELBOW > cloud_yRWRIST):
        if (cloud_xRWRIST > cloud_xLWRIST) and (cloud_xLELBOW > cloud_xRELBOW) :
            print( " It is STOP or NO sign!")
        else:
            print("Person is saying Hi! with both hands!")
    elif cloud_yLELBOW > cloud_yLWRIST:
        print("Person is saying Hi! with left hand :)")
    elif cloud_yRELBOW < cloud_yRWRIST:
        print("Person is saying Hi! with right hand :)")


