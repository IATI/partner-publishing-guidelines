***************************************
How do I link my activity to my funder?
***************************************

Publishing links between your activity and your funder creates traceability — a visible chain from donors through to implementing organisations. You do this in two places in your IATI activity data: participating organisations and transactions.


Steps to complete
-----------------

.. topic:: 1) Find your funder's identifiers
   
   Your funder should give you two identifiers: their IATI organisation reference (e.g. GB-GOV-1) and the IATI activity identifier for the specific     project funding you (e.g. GB-GOV-1-300001). 

If you don't have these identifiers yet, ask your funder or `search activities on d-portal <https://d-portal.iatistandard.org/>`_. You can include your funder's name and organisation type in your publication initially, then add identifiers at a later date.


.. topic:: 2) Add your funder as a participating organisation
   
   Use role = "Funding" (code 1) in the 'participating-org' element of your activity.

Include every organisation involved in the activity — funding, accountable, extending, and implementing. An organisation can hold multiple roles, in which case list it once per role.

Also list your organisation (with role = "Accountable" or "Implementing") and any downstream partners you fund.
   

.. topic:: 3) Add incoming fund or commitment transactions
   
   Reference your funder's activity identifier as the 'provider-activity-id' within each transaction.

Incoming Funds (code 1) = money already received. Incoming Commitment (code 11) = money promised but not yet transferred.

'provider-activity-id' can be found within the 'provider-org' element of a transaction.


.. topic:: 4) Link parent / sibling activities (if applicable)
   
   This is only needed if your activity is part of a programme with multiple sub-activities.

If your organisation runs a programme with multiple activities (e.g. a parent programme and several country-level sub-activities), link them using 'related-activity'.


Checklist before you publish
-----------------------------
- I have my funder's IATI organisation reference
- I have my funder's IATI activity identifier for this project
- My funder is listed under 'participating-org' with role = 1 (Funding)
- Each incoming transaction includes a 'provider-org' with @provider-activity-id
- My own organisation is listed under 'participating-org' (accountable or implementing role)
- I've included my own activity identifier in 'receiver-org' on each incoming transaction

----------------------------------------------------------------------------------------------------------------------------------

Examples
---------

In the example below, the UK Foreign, Commonwealth & Development Office is being referenced as the 'provider organisation' (i.e. funder). 

Within an activity transaction, enter your funder's IATI organisation reference (e.g. "GB-GOV-1" for FCDO), provider activity ID (e.g. "GB-GOV-1-300001" - change the end number accordingly), organisation name and type.

.. figure:: images/iati_publisher_provider_activity_id.png
    :width: 100 %
    :align: center
    :alt: Populating the 'provider activity ID' field within a transaction

    *Figure 1: Where to populate the 'provider activity ID' within a transaction in IATI Publisher*

