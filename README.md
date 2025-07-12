# process_validator
 Implement breach analysis and visualization tools # This commit introduces a set of tools for analyzing and visualizing data breaches.
POC and Synopsis of thesis. 
•	Simulate company workflow data (like purchase process).
•	Analyze that data to see if people followed the standard process.
•	Detect breaches (steps missing or out of order).
•	Highlight those breaches.
•	Explain it clearly as an analysis.

**Defining the Standard Process**
Seq	Activity	Department
1	Issuance of RFQ	Sales
2	Technical Evaluation	Engineering
3	Commercial Evaluation	Sales
4	PO Creation	Procurement
5	Production Planning	Production
6	Parts Manufacturing	Production
7	Packaging & Dispatch	Logistics
8	Goods In Transit	Logistics
9	Goods Receipt at Warehouse	Logistics
10	Quality Inspection	Quality
11	Invoice Generation	Finance
12	Payment Clearance	Finance
**This is the standard path.**

**Design of CSV Structure**
Column	Example Value
Case ID	ORDER-00001
Company	Anish Automobiles
Activity	PO Creation
Sequence	4
Timestamp	2025-01-04 14:00:00
User	Alice
Department	Procurement
Status	Complete / Error


**Planned Breaches: **
We’ll make ~10–15% of orders have issues:
Missing Steps
Out-of-Order Steps
These will be detectable in analysis.
