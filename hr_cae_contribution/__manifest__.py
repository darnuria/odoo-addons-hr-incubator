# Copyright 2019 Coop IT Easy SCRL fs
#   Manuel Claeys Bouuaert <manuel@coopiteasy.be>
# Copyright 2020 GRAP
#   Quentin Dupont <quentin.dupont@grap.coop>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "HR CAE Contribution",
    "summary": "Manage employee contributions and exeptions in a CAE.",
    "author": "Coop IT Easy SCRLfs, GRAP",
    "website": "https://www.coopiteasy.be, http://www.grap.coop",
    "category": "Human Resources",
    "version": "12.0.1.2.0",
    "license": "AGPL-3",
    "depends": ["hr_cae"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee.xml",
        "views/hr_exemption.xml",
    ],
    "installable": True,
    "application": False,
}
