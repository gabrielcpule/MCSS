import React from "react";
import "./mcss-poc.css";
import image from "./image.png";

export default function LoginPage() {
  return (
    <div
      typeof="mcs:Component"
      property="mcs:purpose"
      content="Login page layout with marketing and authentication."
      className="l-stack"
      style={{ minHeight: "100vh", display: "flex", alignItems: "center", justifyContent: "center", background: "#e6f9e6" }}
      data-mcs-interaction-type="layout"
      data-mcs-consequence="Displays login and marketing content side by side."
    >
      <div
        className="l-stack"
        typeof="mcs:Component"
        property="mcs:purpose"
        content="Main content container with marketing and login card."
        style={{ display: "flex", gap: "4rem", alignItems: "center", maxWidth: 1100, width: "100%", justifyContent: "center" }}
        data-mcs-interaction-type="layout"
        data-mcs-consequence="Arranges marketing and login card horizontally."
      >
        {/* Left Side: Illustration and Text */}
        <div
          typeof="mcs:Component"
          property="mcs:purpose"
          content="Marketing message and branding."
          style={{ flex: 1, maxWidth: 480 }}
        >
          <div style={{ marginBottom: 32 }}>
            <span style={{ fontSize: 40, fontWeight: 700, color: "#212529", display: "block", lineHeight: 1.1 }}
              typeof="mcs:Component"
              property="mcs:purpose"
              content="Main heading for sign on."
            >Sign On</span>
            <span style={{ fontSize: 40, fontWeight: 700, color: "#005A9C", background: "#fff", padding: "0 0.5em", borderRadius: 6, boxShadow: "0 2px 0 #2125291a", display: "inline-block", margin: "16px 0 0 0" }}
              typeof="mcs:Component"
              property="mcs:purpose"
              content="Brand highlight for Social."
            >Social</span>
            <span style={{ fontSize: 40, fontWeight: 700, color: "#F44336", display: "block", marginTop: -8 }}
              typeof="mcs:Component"
              property="mcs:purpose"
              content="Brand highlight for Networking."
            >Networking</span>
          </div>
          <div style={{ fontSize: 20, color: "#212529", marginTop: 24, maxWidth: 400 }}
            typeof="mcs:Component"
            property="mcs:purpose"
            content="Marketing subtext."
          >
            Reduce the burden of customers of creating new social accounts for different websites
          </div>
        </div>
        {/* Right Side: Login Card */}
        <div
          className="c-card"
          typeof="mcs:Component"
          property="mcs:purpose"
          content="Login card container."
          style={{ flex: 1, maxWidth: 400, minWidth: 340 }}
        >
          <form
            className="l-stack"
            style={{ padding: 32 }}
            typeof="mcs:Component"
            property="mcs:purpose"
            content="A login form for user authentication."
            autoComplete="off"
            data-mcs-interaction-type="form"
            data-mcs-consequence="Authenticates the user."
          >
            <div className="l-stack" style={{ '--stack-space': '1.5rem' }}>
              <div
                className="c-form-group"
                typeof="mcs:Component"
                property="mcs:purpose"
                content="Email input field for user login."
              >
                <label
                  htmlFor="email"
                  className="c-form-group__label"
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Label for email address input."
                >Email Address</label>
                <input
                  type="email"
                  id="email"
                  className="c-form-group__input"
                  placeholder="username@gmail.com"
                  required
                  aria-required="true"
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Input for user email address."
                  data-mcs-interaction-type="input"
                  data-mcs-consequence="Captures user email."
                />
              </div>
              <div
                className="c-form-group"
                typeof="mcs:Component"
                property="mcs:purpose"
                content="Password input field for user login."
              >
                <label
                  htmlFor="password"
                  className="c-form-group__label"
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Label for password input."
                >Password</label>
                <div style={{ position: "relative" }}>
                  <input
                    type="password"
                    id="password"
                    className="c-form-group__input"
                    placeholder=""
                    required
                    aria-required="true"
                    style={{ paddingRight: 40 }}
                    typeof="mcs:Component"
                    property="mcs:purpose"
                    content="Input for user password."
                    data-mcs-interaction-type="input"
                    data-mcs-consequence="Captures user password."
                  />
                  <span
                    style={{ position: "absolute", right: 10, top: "50%", transform: "translateY(-50%)", color: "#adb5bd", cursor: "pointer" }}
                    aria-label="Show password"
                    tabIndex={0}
                    typeof="mcs:Component"
                    property="mcs:purpose"
                    content="Icon to toggle password visibility."
                    data-mcs-interaction-type="action"
                    data-mcs-consequence="Toggles password visibility."
                  >
                    <svg width="22" height="22" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="8" ry="5"/><circle cx="12" cy="12" r="2.5"/></svg>
                  </span>
                </div>
              </div>
              <div style={{ display: "flex", justifyContent: "flex-end", marginTop: -8 }}>
                <a
                  href="#"
                  className="c-button c-button--secondary"
                  style={{ background: "none", border: "none", color: "#005A9C", fontWeight: 700, fontSize: 14, textDecoration: "underline", padding: 0, minWidth: 0 }}
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Link to reset forgotten password."
                  data-mcs-interaction-type="navigation"
                  data-mcs-consequence="Navigates to password reset."
                >Forgot password?</a>
              </div>
              <button
                type="submit"
                className="c-button c-button--primary"
                style={{ width: "100%", fontSize: 18, marginTop: 8 }}
                typeof="mcs:Component"
                property="mcs:purpose"
                content="Primary action button to log in the user."
                data-mcs-interaction-type="action"
                data-mcs-consequence="Attempts user login."
              >Login</button>
              <div style={{ display: "flex", justifyContent: "center", gap: 16, margin: "16px 0 0 0" }}>
                <a
                  href="#"
                  className="c-button"
                  style={{ background: "#F44336", color: "#fff", border: "none", borderRadius: "50%", width: 44, height: 44, padding: 0, display: "flex", alignItems: "center", justifyContent: "center" }}
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Login with Google."
                  data-mcs-interaction-type="action"
                  data-mcs-consequence="Authenticates with Google."
                ><span style={{ fontSize: 24 }}>G</span></a>
                <a
                  href="#"
                  className="c-button"
                  style={{ background: "#0077b5", color: "#fff", border: "none", borderRadius: "50%", width: 44, height: 44, padding: 0, display: "flex", alignItems: "center", justifyContent: "center" }}
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Login with LinkedIn."
                  data-mcs-interaction-type="action"
                  data-mcs-consequence="Authenticates with LinkedIn."
                ><span style={{ fontSize: 24 }}>in</span></a>
                <a
                  href="#"
                  className="c-button"
                  style={{ background: "#4267B2", color: "#fff", border: "none", borderRadius: "50%", width: 44, height: 44, padding: 0, display: "flex", alignItems: "center", justifyContent: "center" }}
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Login with Facebook."
                  data-mcs-interaction-type="action"
                  data-mcs-consequence="Authenticates with Facebook."
                ><span style={{ fontSize: 24 }}>f</span></a>
                <a
                  href="#"
                  className="c-button"
                  style={{ background: "#212529", color: "#fff", border: "none", borderRadius: "50%", width: 44, height: 44, padding: 0, display: "flex", alignItems: "center", justifyContent: "center" }}
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Login with GitHub."
                  data-mcs-interaction-type="action"
                  data-mcs-consequence="Authenticates with GitHub."
                ><span style={{ fontSize: 24 }}>&#123; &#125;</span></a>
              </div>
              <div style={{ textAlign: "center", marginTop: 16, fontSize: 15 }}>
                Don't have an account?{' '}
                <a
                  href="#"
                  className="c-button c-button--secondary"
                  style={{ background: "none", border: "none", color: "#005A9C", fontWeight: 700, fontSize: 15, textDecoration: "underline", padding: 0, minWidth: 0 }}
                  typeof="mcs:Component"
                  property="mcs:purpose"
                  content="Link to sign up for a new account."
                  data-mcs-interaction-type="navigation"
                  data-mcs-consequence="Navigates to sign up page."
                >Sign Up</a>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
