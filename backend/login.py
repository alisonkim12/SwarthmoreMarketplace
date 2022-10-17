// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBPwmDxLcv11-nhDhmwq1Jqt6Q2sQ9XccY",
  authDomain: "swarthmoremarketplace.firebaseapp.com",
  projectId: "swarthmoremarketplace",
  storageBucket: "swarthmoremarketplace.appspot.com",
  messagingSenderId: "410170758850",
  appId: "1:410170758850:web:efc1a435d0d065d26d4d5b",
  measurementId: "G-1YP7TGS9CT"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

//get list of users database