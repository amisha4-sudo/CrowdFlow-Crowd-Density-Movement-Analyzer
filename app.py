import cv2
import streamlit as st
from detect import detect_people

st.title("CrowdFlow – Crowd Density Analyzer")

run = st.button("Start Camera")

if run:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        count = detect_people(frame)

        st.image(frame, channels="BGR")
        st.write(f"People Count: {count}")

        if count > 10:
            st.warning("Overcrowding detected!")

        if cv2.waitKey(1) == 27:
            break
