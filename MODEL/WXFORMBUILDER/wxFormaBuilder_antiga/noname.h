///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Aug 11 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/sizer.h>
#include <wx/panel.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/radiobut.h>
#include <wx/statbox.h>
#include <wx/treelist.h>
#include <wx/notebook.h>
#include <wx/button.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class JanelaGerenciaPerfis
///////////////////////////////////////////////////////////////////////////////
class JanelaGerenciaPerfis : public wxFrame
{
	private:

	protected:
		wxNotebook* m_notebook1;
		wxPanel* panelInformation;
		wxStaticText* m_staticText1;
		wxTextCtrl* m_textCtrl3;
		wxStaticText* m_staticText2;
		wxTextCtrl* m_textCtrl4;
		wxPanel* panelElevacoes;
		wxStaticText* m_staticText5;
		wxStaticText* m_staticText6;
		wxRadioButton* m_radioBtn2;
		wxTextCtrl* m_textCtrl5;
		wxTextCtrl* m_textCtrl6;
		wxRadioButton* m_radioBtn3;
		wxTextCtrl* m_textCtrl7;
		wxTextCtrl* m_textCtrl8;
		wxPanel* m_panel3;
		wxTreeListCtrl* treeLstCtrl_Elementos;
		wxStdDialogButtonSizer* m_sdbSizer1;
		wxButton* m_sdbSizer1OK;
		wxButton* m_sdbSizer1Cancel;

	public:

		JanelaGerenciaPerfis( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,300 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~JanelaGerenciaPerfis();

};

#endif //__NONAME_H__
