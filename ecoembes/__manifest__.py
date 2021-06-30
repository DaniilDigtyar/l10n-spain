# Copyright 2016 FactorLibre - Janire Olagibel
# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Ecoembes",
    "summary": "Add some data related to ecoembes.com",
    "author": "FactorLibre, Tecnativa, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-spain",
    "license": "AGPL-3",
    "category": "Tools",
    "version": "13.0.1.0.0",
    "depends": ["account"],
    "data": [
        "data/ecoembes.market.type.csv",
        "data/ecoembes.material.csv",
        "data/ecoembes.packaging.csv",
        "data/ecoembes.sector.csv",
        "data/ecoembes.submaterial.csv",
        "security/ir.model.access.csv",
        "views/ecoembes_market_type_view.xml",
        "views/ecoembes_material_view.xml",
        "views/ecoembes_packaging_view.xml",
        "views/ecoembes_sector_view.xml",
        "views/ecoembes_submaterial_view.xml",
        "views/product_product_view.xml",
        "views/product_composition_view.xml",
        "views/res_company_view.xml",
        "report/external_layout.xml",
        "wizard/ecoembes_sig_report_wizard_view.xml",
    ],
    "application": False,
    "installable": True,
}
