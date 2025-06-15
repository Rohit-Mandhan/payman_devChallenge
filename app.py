import streamlit as st
import pandas as pd
import time
from datetime import datetime
from payman_sdk.client import PaymanClient
from payman_sdk.types import PaymanConfig

# — Payman AI Credentials —
PAYMAN_CLIENT_ID = 'pm-test-HbI872xPrsf0pAPlt8T-yYzS'
PAYMAN_CLIENT_SECRET = 'gZNxz0Bp1ePAzZGFabv-X-_sAiuwG9XOJ20FRE6w05OChLQ19uo7PoZLMFG81AyE'

config: PaymanConfig = {
    'client_id': PAYMAN_CLIENT_ID,
    'client_secret': PAYMAN_CLIENT_SECRET,
}
client = PaymanClient.with_credentials(config)

# — Streamlit UI —
st.set_page_config(page_title="Payman Task & Payment Manager", layout="centered")
st.title("💸 Payman: Task Approval & TSD Payment Manager")

# Wallet dropdown
wallet_options = ["taskpay Wallet", "TSD Wallet", "TaskMaster Wallet"]
selected_wallet = st.selectbox("🔐 Select Wallet to Pay From", wallet_options)

uploaded_file = st.file_uploader("📂 Upload CSV (Payee, Amount, Due Date, Category, Account Info, [Optional: Scheduled Date])", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    required = {"Payee", "Amount", "Due Date", "Category", "Account Info"}

    if not required.issubset(df.columns):
        st.error(f"❌ CSV missing required columns: {required}")
    else:
        st.success("✅ CSV loaded")
        approved_rows = []

        for i, row in df.iterrows():
            with st.expander(f"{row['Payee']} — ₹{row['Amount']}"):
                st.write(f"📅 Due: {row['Due Date']}")
                st.write(f"📁 Category: {row['Category']}")
                st.write(f"🏦 Account Info: {row['Account Info']}")

                # Scheduling support
                if "Scheduled Date" in df.columns:
                    scheduled_time = pd.to_datetime(row["Scheduled Date"])
                else:
                    scheduled_time = st.datetime_input("📆 Schedule Payment For:", datetime.now(), key=f"sch_{i}")

                if st.checkbox("✅ Approve", key=f"approve_{i}"):
                    row_data = row.to_dict()
                    row_data["Scheduled Time"] = scheduled_time
                    approved_rows.append(row_data)

        if st.button("🚀 Send Approved Payments"):
            if not approved_rows:
                st.warning("⚠️ No payments approved.")
            else:
                successes = []

                # Fetch payees once
                try:
                    payee_check = client.ask("list payees")
                    payees_text = str(payee_check).lower()
                except Exception as e:
                    st.error(f"❌ Couldn't fetch payee list: {e}")
                    payees_text = ""

                for row in approved_rows:
                    payee_name = row["Payee"]
                    scheduled_time = row["Scheduled Time"]

                    # Skip if scheduled time is in future
                    if datetime.now() < scheduled_time:
                        st.info(f"⏳ Skipping {payee_name} — scheduled for {scheduled_time}")
                        continue

                    # Auto-create payee
                    if payee_name.lower() not in payees_text:
                        try:
                            st.info(f"➕ Creating payee: {payee_name}")
                            creation_resp = client.ask(f"create payee named {payee_name}")
                            st.success(f"✅ Payee created: {creation_resp}")
                            time.sleep(2)
                        except Exception as e:
                            st.error(f"❌ Failed to create payee '{payee_name}': {e}")
                            continue

                    # Send payment
                    msg = (
                        f"send {row['Amount']} TSD to {payee_name} "
                        f"type test rails from {selected_wallet}"
                    )
                    try:
                        resp = client.ask(msg)
                        response_text = str(resp).lower()

                        success_phrases = [
                            "awaiting approval", "payment has been submitted",
                            "payment has been initiated", "status: awaiting approval",
                            "payment request received", "the payment has been sent successfully",
                            "status: payment initiated"
                        ]

                        if any(phrase in response_text for phrase in success_phrases):
                            st.success(f"✅ Payment queued for {payee_name}: {resp}")
                            successes.append(row)
                        elif "error" in response_text or "failed" in response_text:
                            st.error(f"❌ Failed for {payee_name}: {resp}")
                        else:
                            st.info(f"ℹ️ Review response for {payee_name}: {resp}")

                    except Exception as e:
                        st.error(f"❌ Exception for {payee_name}: {e}")

                    time.sleep(3)  # Prevent agent overload

                if successes:
                    st.subheader("📊 Completed Payments")
                    st.dataframe(pd.DataFrame(successes))
else:
    st.info("📂 Upload a properly formatted CSV to start.")
