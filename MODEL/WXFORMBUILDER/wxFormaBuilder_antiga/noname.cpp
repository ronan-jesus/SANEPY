///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Aug 11 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

JanelaGerenciaPerfis::JanelaGerenciaPerfis( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxVERTICAL );

	m_notebook1 = new wxNotebook( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	panelInformation = new wxPanel( m_notebook1, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxVERTICAL );


	bSizer3->Add( 0, 10, 0, wxEXPAND, 5 );

	m_staticText1 = new wxStaticText( panelInformation, wxID_ANY, wxT("Nome:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText1->Wrap( -1 );
	bSizer3->Add( m_staticText1, 0, wxALL, 5 );

	m_textCtrl3 = new wxTextCtrl( panelInformation, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	bSizer3->Add( m_textCtrl3, 0, wxALL|wxEXPAND, 5 );

	m_staticText2 = new wxStaticText( panelInformation, wxID_ANY, wxT("Descrição:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText2->Wrap( -1 );
	bSizer3->Add( m_staticText2, 0, wxALL, 5 );

	m_textCtrl4 = new wxTextCtrl( panelInformation, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( -1,60 ), wxTE_MULTILINE );
	bSizer3->Add( m_textCtrl4, 0, wxALL|wxEXPAND, 5 );


	panelInformation->SetSizer( bSizer3 );
	panelInformation->Layout();
	bSizer3->Fit( panelInformation );
	m_notebook1->AddPage( panelInformation, wxT("Informações"), false );
	panelElevacoes = new wxPanel( m_notebook1, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxStaticBoxSizer* sbSizer1;
	sbSizer1 = new wxStaticBoxSizer( new wxStaticBox( panelElevacoes, wxID_ANY, wxT("Elevações") ), wxVERTICAL );

	wxGridSizer* gSizer1;
	gSizer1 = new wxGridSizer( 3, 3, 0, 0 );


	gSizer1->Add( 0, 0, 0, 0, 5 );

	m_staticText5 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Início:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText5->Wrap( -1 );
	gSizer1->Add( m_staticText5, 0, wxALIGN_BOTTOM|wxLEFT, 5 );

	m_staticText6 = new wxStaticText( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Final:"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText6->Wrap( -1 );
	gSizer1->Add( m_staticText6, 0, wxALIGN_BOTTOM|wxLEFT, 5 );

	m_radioBtn2 = new wxRadioButton( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Automático"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_radioBtn2, 0, wxALL, 5 );

	m_textCtrl5 = new wxTextCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_textCtrl5, 0, wxALL, 5 );

	m_textCtrl6 = new wxTextCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_textCtrl6, 0, wxALL, 5 );

	m_radioBtn3 = new wxRadioButton( sbSizer1->GetStaticBox(), wxID_ANY, wxT("Definido Pelo Usuário"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_radioBtn3, 0, wxALL, 5 );

	m_textCtrl7 = new wxTextCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_textCtrl7, 0, wxALL, 5 );

	m_textCtrl8 = new wxTextCtrl( sbSizer1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_textCtrl8, 0, wxALL, 5 );


	sbSizer1->Add( gSizer1, 0, wxEXPAND, 5 );


	panelElevacoes->SetSizer( sbSizer1 );
	panelElevacoes->Layout();
	sbSizer1->Fit( panelElevacoes );
	m_notebook1->AddPage( panelElevacoes, wxT("Elevações"), false );
	m_panel3 = new wxPanel( m_notebook1, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* self.boxSizerElementos;
	self.boxSizerElementos = new wxBoxSizer( wxVERTICAL );

	treeLstCtrl_Elementos = new wxTreeListCtrl( m_panel3, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTL_CHECKBOX|wxTL_DEFAULT_STYLE|wxBORDER_RAISED|wxBORDER_SIMPLE );

	self.boxSizerElementos->Add( treeLstCtrl_Elementos, 1, wxEXPAND | wxALL, 5 );


	m_panel3->SetSizer( self.boxSizerElementos );
	m_panel3->Layout();
	self.boxSizerElementos->Fit( m_panel3 );
	m_notebook1->AddPage( m_panel3, wxT("Trechos e Estruturas"), true );

	bSizer1->Add( m_notebook1, 1, wxEXPAND | wxALL, 5 );

	m_sdbSizer1 = new wxStdDialogButtonSizer();
	m_sdbSizer1OK = new wxButton( this, wxID_OK );
	m_sdbSizer1->AddButton( m_sdbSizer1OK );
	m_sdbSizer1Cancel = new wxButton( this, wxID_CANCEL );
	m_sdbSizer1->AddButton( m_sdbSizer1Cancel );
	m_sdbSizer1->Realize();

	bSizer1->Add( m_sdbSizer1, 0, wxALIGN_RIGHT|wxEXPAND, 5 );


	this->SetSizer( bSizer1 );
	this->Layout();

	this->Centre( wxBOTH );
}

JanelaGerenciaPerfis::~JanelaGerenciaPerfis()
{
}
