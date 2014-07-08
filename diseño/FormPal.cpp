///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun  6 2014)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "FormPal.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxBoxSizer* bSizer1;
	bSizer1 = new wxBoxSizer( wxHORIZONTAL );
	
	m_splitter1 = new wxSplitterWindow( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxSP_3D );
	m_splitter1->Connect( wxEVT_IDLE, wxIdleEventHandler( MyFrame1::m_splitter1OnIdle ), NULL, this );
	
	m_panel6 = new wxPanel( m_splitter1, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer6;
	bSizer6 = new wxBoxSizer( wxVERTICAL );
	
	m_notebook3 = new wxNotebook( m_panel6, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	m_panel8 = new wxPanel( m_notebook3, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer7;
	bSizer7 = new wxBoxSizer( wxVERTICAL );
	
	m_treeCtrl1 = new wxTreeCtrl( m_panel8, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTR_DEFAULT_STYLE );
	bSizer7->Add( m_treeCtrl1, 0, wxALL, 5 );
	
	
	m_panel8->SetSizer( bSizer7 );
	m_panel8->Layout();
	bSizer7->Fit( m_panel8 );
	m_notebook3->AddPage( m_panel8, wxT("Objetos"), true );
	m_panel9 = new wxPanel( m_notebook3, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	m_notebook3->AddPage( m_panel9, wxT("Datos"), false );
	
	bSizer6->Add( m_notebook3, 1, wxEXPAND | wxALL, 5 );
	
	
	m_panel6->SetSizer( bSizer6 );
	m_panel6->Layout();
	bSizer6->Fit( m_panel6 );
	m_panel7 = new wxPanel( m_splitter1, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );
	
	m_scrolledWindow5 = new wxScrolledWindow( m_panel7, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxALWAYS_SHOW_SB|wxHSCROLL|wxVSCROLL );
	m_scrolledWindow5->SetScrollRate( 5, 5 );
	bSizer5->Add( m_scrolledWindow5, 1, wxEXPAND | wxALL, 5 );
	
	
	m_panel7->SetSizer( bSizer5 );
	m_panel7->Layout();
	bSizer5->Fit( m_panel7 );
	m_splitter1->SplitVertically( m_panel6, m_panel7, 0 );
	bSizer1->Add( m_splitter1, 1, wxEXPAND, 5 );
	
	
	this->SetSizer( bSizer1 );
	this->Layout();
	m_statusBar1 = this->CreateStatusBar( 1, wxST_SIZEGRIP, wxID_ANY );
	m_menubar1 = new wxMenuBar( 0 );
	m_menuArc = new wxMenu();
	wxMenuItem* f2s_menuSalir;
	f2s_menuSalir = new wxMenuItem( m_menuArc, wxID_ANY, wxString( wxT("Salir") ) + wxT('\t') + wxT("CTRL X"), wxEmptyString, wxITEM_NORMAL );
	m_menuArc->Append( f2s_menuSalir );
	
	m_menubar1->Append( m_menuArc, wxT("Archivo") ); 
	
	this->SetMenuBar( m_menubar1 );
	
	m_auiToolBar1 = new wxAuiToolBar( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxAUI_TB_HORZ_LAYOUT ); 
	m_tool1 = m_auiToolBar1->AddTool( wxID_ANY, wxT("tool"), wxNullBitmap, wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString, NULL ); 
	
	m_auiToolBar1->AddSeparator(); 
	
	m_tool2 = m_auiToolBar1->AddTool( wxID_ANY, wxT("tool"), wxNullBitmap, wxNullBitmap, wxITEM_NORMAL, wxEmptyString, wxEmptyString, NULL ); 
	
	m_auiToolBar1->Realize(); 
	
	
	this->Centre( wxBOTH );
}

MyFrame1::~MyFrame1()
{
}

f2s_DiagTexto::f2s_DiagTexto( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxDialog( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	this->SetFont( wxFont( 11, 74, 90, 90, false, wxT("Sans") ) );
	
	wxBoxSizer* bSizer8;
	bSizer8 = new wxBoxSizer( wxVERTICAL );
	
	m_propertyGrid1 = new wxPropertyGrid(this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxPG_DEFAULT_STYLE|wxALWAYS_SHOW_SB|wxHSCROLL|wxRAISED_BORDER|wxVSCROLL);
	bSizer8->Add( m_propertyGrid1, 0, wxALL, 5 );
	
	wxBoxSizer* bSizer9;
	bSizer9 = new wxBoxSizer( wxHORIZONTAL );
	
	m_button2 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer9->Add( m_button2, 0, wxALL, 5 );
	
	m_button3 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer9->Add( m_button3, 0, wxALL, 5 );
	
	m_button4 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer9->Add( m_button4, 0, wxALL, 5 );
	
	
	bSizer8->Add( bSizer9, 1, wxEXPAND, 5 );
	
	
	this->SetSizer( bSizer8 );
	this->Layout();
	bSizer8->Fit( this );
	
	this->Centre( wxBOTH );
}

f2s_DiagTexto::~f2s_DiagTexto()
{
}
