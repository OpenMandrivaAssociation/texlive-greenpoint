# revision 15878
# category Package
# catalog-ctan /fonts/greenpoint
# catalog-date 2006-12-09 16:48:33 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-greenpoint
Version:	20061209
Release:	2
Summary:	The Green Point logo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greenpoint
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greenpoint.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greenpoint.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A MetaFont-implementation of the logo commonly known as 'Der
Grune Punkt' ('The Green Point'). In Austria, it can be found
on nearly every bottle. It should not be confused with the
'Recycle'-logo, implemented by Ian Green.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/greenpoint/greenpoint.mf
%{_texmfdistdir}/fonts/tfm/public/greenpoint/greenpoint.tfm
%doc %{_texmfdistdir}/doc/fonts/greenpoint/ChangeLog
%doc %{_texmfdistdir}/doc/fonts/greenpoint/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061209-2
+ Revision: 752436
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061209-1
+ Revision: 718583
- texlive-greenpoint
- texlive-greenpoint
- texlive-greenpoint
- texlive-greenpoint

