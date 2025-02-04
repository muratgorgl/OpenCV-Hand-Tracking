import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands

hands = mpHand.Hands()

mpDraw = mp.solutions.drawing_utils
pTime = 0 
cTime = 0 


while True:
    ret, frame = cap.read() 
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handLms, mpHand.HAND_CONNECTIONS)
             
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = frame.shape
                
                cx, cy = int(lm.x * w), int (lm.y * h)
                
                #bilek
                if id == 20:
                    cv2.circle(frame, (cx,cy), 9, (255,0,0), cv2.FILLED)
                                 
                
    # fps 
    cTime = time.time()
    fps = 1 / (cTime-pTime) 
    pTime= cTime

    cv2.putText(frame, "FPS: " + str(int(fps)), (10,75), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 5 )           
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"): break
    
cap.release()
cv2.destroyAllWindows()