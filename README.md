# payman_devChallenge
# ✈️ PayPilot: Smart Task Approvals with Automated Payments via Payman SDK

A fully functional AI-ready automation system that streamlines task management and executes **secure, verified TSD payments** using the **Payman SDK**. Built for the **Payman AI Developer Challenge #2**, this project showcases a real-world use case where payments are triggered only after manual task approval — ideal for freelancing platforms, gig workers, or internal project workflows.

---

## 🚀 Key Features

* 📄 **CSV Upload**: Import a task list with assignees, payment amounts, and task details.
* ✅ **Manual Task Approval Flow**: Review tasks and approve/reject them within the app.
* 💸 **TSD Payment Integration**: Auto-send payments to approved users using Payman's TSD system.
* 🔐 **Auto Payee Creation**: Automatically creates payee profiles and links them to wallets if needed.
* 🔀 **Payment Queueing**: Handles queued payments and avoids duplicate transactions.
* 📡 **Real-time Transaction Tracking**: Verifies and logs Payman transaction status for transparency.
* 📊 **Streamlit UI**: Built with a clean and minimal interface for quick deployment and testing.

---

## 🧠 Why This Matters

> In the real world, not every task should be paid immediately. This app offers a **"review-first, pay-later"** pipeline that mimics real business logic, while seamlessly integrating with Payman's programmable finance infrastructure.

---

## 📂 How It Works

1. **Upload CSV**
   Format:

   ```
   name,email,task_description,amount
   John Doe,john@example.com,Design Logo,50
   Jane Smith,jane@example.com,Write Blog,75
   ```

2. **Approve Tasks**
   Use the UI to approve/reject tasks based on your review.

3. **Trigger Payments**
   Upon approval, the app:

   * Checks if a wallet/payee exists
   * Creates one if needed
   * Sends the TSD payment
   * Verifies transaction status

---

## 🛠️ Tech Stack

* **Streamlit** – Fast UI prototyping
* **Python** – Backend logic
* **Payman SDK (payman-ts)** – TSD transactions & wallet management
* **Payman OAuth & API** – Secure and compliant integrations

---

## 🧪 Local Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/paypilot.git
   cd paypilot
   ```

2. Create a virtual environment & install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your environment variables:

   * `PAYMAN_CLIENT_ID`
   * `PAYMAN_CLIENT_SECRET`
   * `PAYMAN_AGENT_ID`

4. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## 🎥 Demo Video (Optional but Recommended)

> \[Link to your Loom/YouTube demo here once recorded]

---

## 🏑 Status

✅ Fully working prototype
⚙️ Ready for Payman submission
🔜 Optional: Add AI-based auto-approval in v2

---

## 🤝 Built For

**Payman AI Developer Challenge – June 2025**
Challenge Theme: *"Build AI-powered finance tools with real-world impact."*

---

## 👤 Author

**Rohit Mandhan**
Email: \[[rohitmandhan2222@gmail.com](mailto:rohitmandhan2222@gmail.com)]

---

## 📜 License

MIT License – Free to use and adapt.
