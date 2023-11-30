import streamlit as st
import subprocess

command = ["python", "run.py", "--mode", "test", "--log_dir", "results", "--config", "config/hdac.yaml", "--checkpoint", "cpks/hdac.pt"] #command to run HDAC
st.header("HDAC - Hybrid Deep Animation Codec")
st.subheader("HDAC is a hybrid model utilizing deep learning and conventional video codecs.")
st.subheader("It specializes in improving the quality of videos in a low bitrate environments, such as poor internet connection.") #headers

st.write("------------------------")

st.write('<span style="font-size: 18px;">Comparions between original low-quality videos and refined videos produced by HDAC</span>', unsafe_allow_html=True)
st.video("videos/1-comparison.mp4")
st.video("videos/2-comparison.mp4")
st.write('<span style="font-size: 18px;">Video demonstrationg the keypoints HDAC uses during refinement</span>', unsafe_allow_html=True)
st.video("videos/3-keypoints.mp4")

if st.button("Run HDAC Model"):
    try:
        subprocess.run(command) #run HDAC command
        st.success("HDAC is now running. Check the console for the status of the process. " +
        "The produced videos will be in the results directory. Press Control + C to stop the execution.")
    except Exception as e:
        st.error(f"Error running HDAC: {e}")
