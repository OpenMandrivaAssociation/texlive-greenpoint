Name:		texlive-greenpoint
Version:	15878
Release:	2
Summary:	The Green Point logo
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greenpoint
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greenpoint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greenpoint.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
