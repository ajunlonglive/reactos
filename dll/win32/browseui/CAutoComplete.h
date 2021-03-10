/*
 *  AutoComplete interfaces implementation.
 *
 *  Copyright 2004  Maxime Belleng� <maxime.bellenge@laposte.net>
 *  Copyright 2009  Andrew Hill
 *  Copyright 2021  Katayama Hirofumi MZ <katayama.hirofumi.mz@gmail.com>
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */
#pragma once

#include "atltypes.h"
#include "rosctrls.h"

class CACEditCtrl;
class CACListView;
class CACScrollBar;
class CACSizeBox;
class CAutoComplete;

//////////////////////////////////////////////////////////////////////////////
// CACEditCtrl --- auto-completion textbox

class CACEditCtrl
    : public CWindowImpl<CACEditCtrl, CWindow, CControlWinTraits>
{
public:
    CAutoComplete* m_pDropDown;
    static LPCWSTR GetWndClassName() { return WC_EDITW; }

    CACEditCtrl();
    VOID HookWordBreakProc(BOOL bHook);

    // message map
    BEGIN_MSG_MAP(CACEditCtrl)
        MESSAGE_HANDLER(WM_CHAR, OnChar)
        MESSAGE_HANDLER(WM_CLEAR, OnCutPasteClear)
        MESSAGE_HANDLER(WM_CUT, OnCutPasteClear)
        MESSAGE_HANDLER(WM_DESTROY, OnDestroy)
        MESSAGE_HANDLER(WM_GETDLGCODE, OnGetDlgCode)
        MESSAGE_HANDLER(WM_KEYDOWN, OnKeyDown)
        MESSAGE_HANDLER(WM_KILLFOCUS, OnKillFocus)
        MESSAGE_HANDLER(WM_PASTE, OnCutPasteClear)
        MESSAGE_HANDLER(WM_SETFOCUS, OnSetFocus)
        MESSAGE_HANDLER(WM_SETTEXT, OnSetText)
    END_MSG_MAP()

protected:
    // protected variables
    EDITWORDBREAKPROCW m_fnOldWordBreakProc;
    // message handlers
    LRESULT OnChar(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnCutPasteClear(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnDestroy(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnGetDlgCode(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnKeyDown(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnKillFocus(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnSetFocus(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnSetText(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
};

//////////////////////////////////////////////////////////////////////////////
// CACListView --- auto-completion list control

class CACListView : public CWindowImpl<CACListView, CListView>
{
public:
    CAutoComplete* m_pDropDown;
    INT m_cyItem;
    static LPCWSTR GetWndClassName() { return WC_LISTVIEW; }

    CACListView();
    HWND Create(HWND hwndParent);
    VOID SetFont(HFONT hFont);

    INT GetVisibleCount();
    CStringW GetItemText(INT iItem);
    INT ItemFromPoint(INT x, INT y);

    INT GetCurSel();
    VOID SetCurSel(INT iItem);
    VOID SelectHere(INT x, INT y);

protected:
    // message map
    BEGIN_MSG_MAP(CACListView)
        MESSAGE_HANDLER(WM_LBUTTONDOWN, OnLButtonDown)
        MESSAGE_HANDLER(WM_LBUTTONUP, OnButtonUp)
        MESSAGE_HANDLER(WM_MBUTTONDOWN, OnMRButtonDown)
        MESSAGE_HANDLER(WM_MBUTTONUP, OnButtonUp)
        MESSAGE_HANDLER(WM_MOUSEWHEEL, OnMouseWheel)
        MESSAGE_HANDLER(WM_NCHITTEST, OnNCHitTest)
        MESSAGE_HANDLER(WM_RBUTTONDOWN, OnMRButtonDown)
        MESSAGE_HANDLER(WM_RBUTTONUP, OnButtonUp)
    END_MSG_MAP()
    // message handlers
    LRESULT OnButtonUp(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnLButtonDown(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnMRButtonDown(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnMouseWheel(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnNCHitTest(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
};

//////////////////////////////////////////////////////////////////////////////
// CACScrollBar --- auto-completion scrollbar control

class CACScrollBar : public CWindowImpl<CACScrollBar>
{
public:
    CAutoComplete* m_pDropDown;
    static LPCWSTR GetWndClassName() { return WC_SCROLLBARW; }

    CACScrollBar();
    HWND Create(HWND hwndParent);

protected:
    // message map
    BEGIN_MSG_MAP(CACScrollBar)
    END_MSG_MAP()
};

//////////////////////////////////////////////////////////////////////////////
// CACSizeBox --- auto-completion size-box control

class CACSizeBox : public CWindowImpl<CACSizeBox>
{
public:
    CAutoComplete* m_pDropDown;
    static LPCWSTR GetWndClassName() { return WC_SCROLLBARW; }

    CACSizeBox();
    HWND Create(HWND hwndParent);
    VOID SetStatus(BOOL bDowner, BOOL bLongList);

protected:
    // protected variables
    BOOL m_bDowner;
    BOOL m_bLongList;
    // message map
    BEGIN_MSG_MAP(CACSizeBox)
        MESSAGE_HANDLER(WM_ERASEBKGND, OnEraseBkGnd)
        MESSAGE_HANDLER(WM_NCHITTEST, OnNCHitTest)
        MESSAGE_HANDLER(WM_PAINT, OnPaint)
    END_MSG_MAP()
    // message handlers
    LRESULT OnEraseBkGnd(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnNCHitTest(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnPaint(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
};

//////////////////////////////////////////////////////////////////////////////
// CAutoComplete --- auto-completion drop-down window

#define WC_DROPDOWNW L"Auto-Suggest Dropdown" // the window class name

class CAutoComplete
    : public CComCoClass<CAutoComplete, &CLSID_AutoComplete>
    , public CComObjectRootEx<CComMultiThreadModelNoCS>
    , public CWindowImpl<CAutoComplete>
    , public IAutoComplete2
    , public IAutoCompleteDropDown
    , public IEnumString
{
public:
    DECLARE_WND_CLASS_EX(WC_DROPDOWNW, CS_DROPSHADOW | CS_SAVEBITS, COLOR_3DFACE)
    static LPCWSTR GetWndClassName() { return WC_DROPDOWNW; }
    BOOL m_bInSetText; // this flag avoids subsequent action in WM_SETTEXT
    BOOL m_bInSelectItem; // this flag avoids subsequent action in LVN_ITEMCHANGED

    // public methods
    CAutoComplete();
    HWND CreateDropDown();
    virtual ~CAutoComplete();

    BOOL CanAutoSuggest();
    BOOL CanAutoAppend();
    BOOL UseTab();
    BOOL IsComboBoxDropped();
    INT GetItemCount();
    CStringW GetItemText(INT iItem);

    CStringW GetEditText();
    VOID SetEditText(LPCWSTR pszText);
    CStringW GetStemText();
    VOID SetEditSel(INT ich0, INT ich1);

    VOID ShowDropDown();
    VOID HideDropDown();
    VOID SelectItem(INT iItem);
    VOID DoAutoAppend();
    VOID DoBackWord();
    VOID UpdateScrollBar();

    LRESULT OnEditChar(WPARAM wParam, LPARAM lParam);
    BOOL OnEditKeyDown(WPARAM wParam, LPARAM lParam);
    VOID OnEditUpdate(BOOL bAppendOK);
    VOID OnListSelChange();
    BOOL OnListUpDown(UINT vk);

    // IAutoComplete methods
    STDMETHODIMP Enable(BOOL fEnable) override;
    STDMETHODIMP Init(HWND hwndEdit, IUnknown *punkACL, LPCOLESTR pwszRegKeyPath,
                      LPCOLESTR pwszQuickComplete) override;
    // IAutoComplete2 methods
    STDMETHODIMP GetOptions(DWORD *pdwFlag) override;
    STDMETHODIMP SetOptions(DWORD dwFlag) override;
    // IAutoCompleteDropDown methods
    STDMETHODIMP GetDropDownStatus(DWORD *pdwFlags, LPWSTR *ppwszString) override;
    STDMETHODIMP ResetEnumerator() override;
    // IEnumString methods
    STDMETHODIMP Next(ULONG celt, LPOLESTR *rgelt, ULONG *pceltFetched) override;
    STDMETHODIMP Skip(ULONG celt) override;
    STDMETHODIMP Reset() override;
    STDMETHODIMP Clone(IEnumString **ppOut) override;

protected:
    // The following variables are POD (plain old data):
    BOOL m_bDowner; // downer or upper? (below textbox or above textbox)
    DWORD m_dwOptions; // for IAutoComplete2::SetOptions
    DWORD m_bEnabled; // the auto-composition is enabled?
    HWND m_hwndCombo; // the combobox if any
    HFONT m_hFont; // the font
    BOOL m_bResized; // re-sized by size-box?
    RECT m_rcEdit; // in screen coordinates, to watch the position
    // The following variables are non-POD:
    CStringW m_strText; // internal text (used in selecting item and reverting text)
    CStringW m_strStemText; // dirname + '\\'
    CStringW m_strQuickComplete; // used for [Ctrl]+[Enter]
    CACEditCtrl m_hwndEdit; // subclassed to watch
    CACListView m_hwndList; // this listview is virtual
    CACScrollBar m_hwndScrollBar; // scroll bar contol
    CACSizeBox m_hwndSizeBox; // the size grip
    CComPtr<IEnumString> m_pEnum; // used for enumeration
    CComPtr<IACList> m_pACList; // for IACList::Expand to update the list
    CSimpleArray<CStringW> m_innerList; // internal list
    CSimpleArray<CStringW> m_outerList; // owner data for virtual listview
    // protected methods
    VOID UpdateDropDownState();
    VOID CalcRects(BOOL bDowner, RECT& rcListView, RECT& rcScrollBar, RECT& rcSizeBox);
    VOID LoadQuickComplete(LPCWSTR pwszRegKeyPath, LPCWSTR pwszQuickComplete);
    CStringW GetQuickEdit(LPCWSTR pszText);
    VOID RepositionDropDown();
    INT ReLoadInnerList();
    INT UpdateInnerList();
    INT UpdateOuterList();
    VOID UpdateCompletion(BOOL bAppendOK);
    // message map
    BEGIN_MSG_MAP(CAutoComplete)
        MESSAGE_HANDLER(WM_CREATE, OnCreate)
        MESSAGE_HANDLER(WM_DESTROY, OnDestroy)
        MESSAGE_HANDLER(WM_DRAWITEM, OnDrawItem)
        MESSAGE_HANDLER(WM_EXITSIZEMOVE, OnExitSizeMove)
        MESSAGE_HANDLER(WM_GETMINMAXINFO, OnGetMinMaxInfo)
        MESSAGE_HANDLER(WM_MEASUREITEM, OnMeasureItem)
        MESSAGE_HANDLER(WM_MOUSEACTIVATE, OnMouseActivate)
        MESSAGE_HANDLER(WM_NCACTIVATE, OnNCActivate)
        MESSAGE_HANDLER(WM_NCLBUTTONDOWN, OnNCLButtonDown)
        MESSAGE_HANDLER(WM_NOTIFY, OnNotify)
        MESSAGE_HANDLER(WM_NCHITTEST, OnNCHitTest)
        MESSAGE_HANDLER(WM_SIZE, OnSize)
        MESSAGE_HANDLER(WM_SHOWWINDOW, OnShowWindow)
        MESSAGE_HANDLER(WM_TIMER, OnTimer)
        MESSAGE_HANDLER(WM_VSCROLL, OnVScroll)
    END_MSG_MAP()
    // message handlers
    LRESULT OnCreate(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnDestroy(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnDrawItem(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnExitSizeMove(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnGetMinMaxInfo(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnMeasureItem(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnMouseActivate(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnNCActivate(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnNCLButtonDown(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnNotify(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnNCHitTest(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnSize(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnShowWindow(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnTimer(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);
    LRESULT OnVScroll(UINT uMsg, WPARAM wParam, LPARAM lParam, BOOL &bHandled);

    DECLARE_REGISTRY_RESOURCEID(IDR_AUTOCOMPLETE)
    DECLARE_NOT_AGGREGATABLE(CAutoComplete)
    DECLARE_PROTECT_FINAL_CONSTRUCT()

    BEGIN_COM_MAP(CAutoComplete)
        COM_INTERFACE_ENTRY_IID(IID_IAutoComplete, IAutoComplete)
        COM_INTERFACE_ENTRY_IID(IID_IAutoComplete2, IAutoComplete2)
        COM_INTERFACE_ENTRY_IID(IID_IAutoCompleteDropDown, IAutoCompleteDropDown)
        COM_INTERFACE_ENTRY_IID(IID_IEnumString, IEnumString)
    END_COM_MAP()
};
