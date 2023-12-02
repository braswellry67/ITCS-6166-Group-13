import streamlit as st
import pandas as pd
import subprocess
command = ["python", "run.py", "--mode", "test", "--log_dir", "results", "--config", "config/hdac.yaml", "--checkpoint", "cpks/hdac.pt", ">", "metrics.txt"] # Command to run HDAC
metrics = { #metrics for table taken from HDAC output logs
    "psnr": 30.208308696746826,
    "lpips": 0.08447073044953868,
    "dists": 0.15696416733165583,
    "msVGG": 77.64462033461314,
    "fsim": 0.9274174626916647,
    "ms_ssim": 0.9283466177682081,
    "vmaf": 38.07265036458333,
    "bitrate": 13.20495575221239
}

# Sidebar navigation menu
selected_page = st.sidebar.radio("Pages", ["HDAC Overview", "HDAC's Performance"])

# First page
if selected_page == "HDAC Overview":
    st.title("HDAC Overview")
    st.subheader("HDAC, the Hybrid Deep-Animation Codec, is a hybrid model utilizing deep learning and conventional video codecs.")
    st.subheader("It specializes in improving the quality of videos in low bitrate environments, such as poor internet connections.")
    
    st.image("images/hdac.jpg", caption="HDAC Framework")
    st.subheader("HDAC consists of three main parts: The Animation Module, Conventional Video Codec, and Fusion Module, each with their own unique function.")
    st.subheader("The below graph shows a comparison between HDAC and other deep learning models based on PSNR. Note how HDAC performs best at low bitrate.")
    st.image("images/hdac2.png", caption="HDAC Comparison")
    
    st.subheader("Continue to the next page on the left to see what HDAC is capable of and run it yourself.")

# Second page
elif selected_page == "HDAC's Performance":
    st.title("HDAC's Peformance")
    st.subheader("HDAC produces two main forms of output: evaluation metrics, and updated videos.")
    st.write("--------------------------------------------")
    st.subheader("The metrics are a quantification of various aspects, such as the bitrate and data points such as lpips and msVGG. An example of this can be seen in the table below.")
    st.subheader("Three videos are produced based on the provided dataset and can be seen in greater detail below.")
    st.write("--------------------------------------------")
    
    st.subheader('Comparisons between original low-quality videos and refined videos produced by HDAC')
    st.video("videos/1-comparison.mp4")
    st.video("videos/2-comparison.mp4")  
    st.subheader('Video demonstrating the keypoints HDAC uses during refinement')
    st.video("videos/3-keypoints.mp4")
    
    st.subheader('Sample metric data')
    df_metrics = pd.DataFrame(list(metrics.items()), columns=['Metric', 'Value'])
    st.table(df_metrics)

    st.subheader('Click the button below to run HDAC. It will output metrics and videos after each iteration.')
    st.subheader('The status of the process can be monitored in the terminal. Control + C to stop execution.')
    if st.button("Run HDAC"): #Start HDAC button
        try:
            subprocess.run(command) # Run HDAC command
            st.success("HDAC is now running. Check the console for the status of the process.")
        except Exception as e:
            st.error(f"Error running HDAC: {e}")          
