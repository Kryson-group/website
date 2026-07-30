/**
 * Kryson Limited — Enquiry Form + Stripe Webhook → Google Sheets
 *
 * SETUP INSTRUCTIONS:
 *
 * 1. Open Google Sheets → Extensions → Apps Script
 * 2. Paste this file, save, and deploy as Web App (Execute as: Me, Access: Anyone)
 * 3. Copy the Web App URL into gen.py as APPS_SCRIPT_URL
 * 4. In Stripe Dashboard → Developers → Webhooks → Add endpoint:
 *    - URL: your Apps Script Web App URL (same one)
 *    - Events: payment_intent.succeeded
 * 5. Run python3 gen.py to rebuild pages
 *
 * This script handles TWO types of incoming POST requests:
 *   - Enquiry form submissions (from the website contact form / modal)
 *   - Stripe webhook events (payment_intent.succeeded)
 */

var SHEET_NAME      = 'Applications';
var NOTIFY_EMAIL    = 'kyle@krysongroup.com';
var CALENDLY_LINK   = 'https://calendly.com/kyle-krysongroup/kryson-limited-website-kick-off-call';
var SITE_URL        = 'https://krysonlimited.com';

// ============================================================
// MAIN HANDLER
// ============================================================

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    var body = JSON.parse(e.postData.contents);

    // Route: Stripe webhook vs. enquiry form
    if (body.type && body.type === 'payment_intent.succeeded') {
      return handleStripePayment(body);
    } else {
      return handleEnquiry(body);
    }

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'error', error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// ============================================================
// ENQUIRY FORM SUBMISSION
// ============================================================

function handleEnquiry(data) {
  var ss    = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);

  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    var headers = ['Timestamp','First Name','Last Name','Email','Phone','Business Type','Package','Message','Source'];
    sheet.appendRow(headers);
    sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold').setBackground('#111827').setFontColor('#ffffff');
    sheet.setFrozenRows(1);
  }

  sheet.appendRow([
    new Date().toISOString(),
    data.firstName    || '',
    data.lastName     || '',
    data.email        || '',
    data.phone        || '',
    data.businessType || '',
    data.package      || '',
    data.message      || '',
    'Enquiry Form'
  ]);

  // Notify Kyle
  GmailApp.sendEmail(
    NOTIFY_EMAIL,
    'New Enquiry: ' + (data.firstName || '') + ' ' + (data.lastName || '') + ' — ' + (data.businessType || 'Unknown'),
    'New enquiry from the Kryson website:\n\n'
    + 'Name: ' + (data.firstName || '') + ' ' + (data.lastName || '') + '\n'
    + 'Email: ' + (data.email || '') + '\n'
    + 'Phone: ' + (data.phone || '') + '\n'
    + 'Business Type: ' + (data.businessType || '') + '\n'
    + 'Package Interest: ' + (data.package || '') + '\n'
    + 'Message: ' + (data.message || '') + '\n\n'
    + 'Submitted at: ' + new Date().toString()
  );

  // Auto-reply to the client
  if (data.email) {
    GmailApp.sendEmail(
      data.email,
      'We received your enquiry — Kryson Web Design',
      'Hi ' + (data.firstName || 'there') + ',\n\n'
      + 'Thanks for getting in touch with Kryson. We\'ve received your enquiry and will be in touch within 24 hours to discuss your website.\n\n'
      + 'In the meantime, feel free to book a kick-off call directly using the link below — it\'s a 30-minute call where we\'ll cover your goals, design preferences, and next steps.\n\n'
      + 'Book your call: ' + CALENDLY_LINK + '\n\n'
      + 'Talk soon,\n'
      + 'Kyle\n'
      + 'Kryson Web Design\n'
      + 'kyle@krysongroup.com\n'
      + SITE_URL,
      {
        name: 'Kyle at Kryson',
        replyTo: NOTIFY_EMAIL
      }
    );
  }

  return ContentService
    .createTextOutput(JSON.stringify({ result: 'success' }))
    .setMimeType(ContentService.MimeType.JSON);
}

// ============================================================
// STRIPE PAYMENT WEBHOOK
// ============================================================

function handleStripePayment(body) {
  var pi     = body.data && body.data.object ? body.data.object : {};
  var email  = pi.receipt_email || (pi.charges && pi.charges.data && pi.charges.data[0] ? pi.charges.data[0].billing_details.email : '');
  var name   = pi.charges && pi.charges.data && pi.charges.data[0] ? pi.charges.data[0].billing_details.name : '';
  var amount = pi.amount ? ('€' + (pi.amount / 100).toFixed(2)) : '';

  // Log to sheet
  var ss    = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);

  sheet.appendRow([
    new Date().toISOString(),
    name,
    '',
    email,
    '',
    '',
    amount,
    '',
    'Stripe Payment'
  ]);

  // Notify Kyle
  GmailApp.sendEmail(
    NOTIFY_EMAIL,
    'New Payment: ' + amount + ' — ' + (name || email || 'Unknown client'),
    'A payment was just completed on the Kryson website.\n\n'
    + 'Client: ' + (name || 'Unknown') + '\n'
    + 'Email: ' + (email || 'Unknown') + '\n'
    + 'Amount: ' + amount + '\n'
    + 'Payment ID: ' + (pi.id || '') + '\n\n'
    + 'They have been sent an email with the Calendly kick-off call link.'
  );

  // Confirmation email to client
  if (email) {
    GmailApp.sendEmail(
      email,
      'Payment confirmed — let\'s schedule your kick-off call | Kryson',
      'Hi ' + (name ? name.split(' ')[0] : 'there') + ',\n\n'
      + 'Your payment of ' + amount + ' has been confirmed — thank you for choosing Kryson!\n\n'
      + 'The next step is to book your kick-off call. This is a 30–45 minute call where we\'ll discuss:\n'
      + '  • Your brand, goals, and design preferences\n'
      + '  • The pages and content your site needs\n'
      + '  • Any integrations (bookings, payments, etc.)\n'
      + '  • Timeline and delivery process\n\n'
      + 'Book your kick-off call here:\n'
      + CALENDLY_LINK + '\n\n'
      + 'We\'re looking forward to building something great for you.\n\n'
      + 'Talk soon,\n'
      + 'Kyle\n'
      + 'Kryson Web Design\n'
      + 'kyle@krysongroup.com\n'
      + SITE_URL,
      {
        name: 'Kyle at Kryson',
        replyTo: NOTIFY_EMAIL
      }
    );
  }

  return ContentService
    .createTextOutput(JSON.stringify({ result: 'success' }))
    .setMimeType(ContentService.MimeType.JSON);
}

// ============================================================
// GET — health check
// ============================================================

function doGet(e) {
  return ContentService
    .createTextOutput('Kryson endpoint is live.')
    .setMimeType(ContentService.MimeType.TEXT);
}
