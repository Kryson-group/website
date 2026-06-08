/**
 * Kryson Limited — Application Form → Google Sheets
 *
 * SETUP INSTRUCTIONS (takes ~2 minutes):
 *
 * 1. Open Google Sheets and create a new spreadsheet named "Kryson Applications"
 * 2. Click Extensions → Apps Script
 * 3. Delete all existing code and paste THIS entire file
 * 4. Click Save (Ctrl+S)
 * 5. Click Deploy → New deployment
 * 6. Type: Web app
 * 7. Execute as: Me
 * 8. Who has access: Anyone
 * 9. Click Deploy → copy the Web App URL
 * 10. Open gen.py and replace:
 *     APPS_SCRIPT_URL = 'YOUR_APPS_SCRIPT_URL_HERE'
 *     with:
 *     APPS_SCRIPT_URL = 'https://script.google.com/macros/s/YOUR_ACTUAL_ID/exec'
 * 11. Run python3 gen.py to rebuild the pages
 *
 * The sheet will auto-create these columns:
 * Timestamp | First Name | Last Name | Email | Phone | Monthly Revenue | Bottleneck | Timeline | Qualified
 */

var SHEET_NAME = 'Applications';

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName(SHEET_NAME);

    // Create sheet and headers if it doesn't exist
    if (!sheet) {
      sheet = ss.insertSheet(SHEET_NAME);
      var headers = [
        'Timestamp',
        'First Name',
        'Last Name',
        'Email',
        'Phone',
        'Monthly Revenue',
        'Bottleneck',
        'Timeline',
        'Qualified'
      ];
      sheet.appendRow(headers);
      sheet.getRange(1, 1, 1, headers.length)
           .setFontWeight('bold')
           .setBackground('#1a1a1a')
           .setFontColor('#c9a84c');
      sheet.setFrozenRows(1);
    }

    // Parse the incoming JSON body
    var data = JSON.parse(e.postData.contents);

    var revenueLabel = {
      'low':  'Under £10k/mo',
      'mid':  '£10k–£30k/mo',
      'high': '£30k–£80k/mo',
      'top':  'Over £80k/mo'
    }[data.monthlyRevenue] || data.monthlyRevenue;

    var qualified = (data.monthlyRevenue !== 'low') ? 'YES' : 'NO – DQ';

    var row = [
      new Date().toISOString(),
      data.firstName   || '',
      data.lastName    || '',
      data.email       || '',
      data.phone       || '',
      revenueLabel,
      data.bottleneck  || '',
      data.timeline    || '',
      qualified
    ];

    sheet.appendRow(row);

    // Colour DQ rows red so they stand out
    if (qualified === 'NO – DQ') {
      var lastRow = sheet.getLastRow();
      sheet.getRange(lastRow, 1, 1, row.length)
           .setBackground('#2a0a0a')
           .setFontColor('#ff6b6b');
    }

    return ContentService
      .createTextOutput(JSON.stringify({ result: 'success' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'error', error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// GET handler — returns a simple health check
function doGet(e) {
  return ContentService
    .createTextOutput('Kryson application endpoint is live.')
    .setMimeType(ContentService.MimeType.TEXT);
}
