#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-fastercsv
Version  : 1.5.5
Release  : 6
URL      : https://rubygems.org/downloads/fastercsv-1.5.5.gem
Source0  : https://rubygems.org/downloads/fastercsv-1.5.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= Read Me
by James Edward Gray II
== Description
Welcome to FasterCSV.
FasterCSV is intended as a replacement to Ruby's standard CSV library.  It was designed to address concerns users of that library had and it has three primary goals:

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n fastercsv-1.5.5
gem spec %{SOURCE0} -l --ruby > rubygem-fastercsv.gemspec

%build
gem build rubygem-fastercsv.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
fastercsv-1.5.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/fastercsv-1.5.5 && ruby -I.:lib:test test/tc_*.rb && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/fastercsv-1.5.5.gem
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/AUTHORS
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/CHANGELOG
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/COPYING
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/INSTALL
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/README
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/TODO
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/examples/csv_converters.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/examples/csv_filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/examples/csv_reading.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/examples/csv_table.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/examples/csv_writing.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/examples/purchase.csv
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/examples/shortcut_interface.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/lib/faster_csv.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/lib/fastercsv.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/line_endings.gz
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_csv_parsing.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_csv_writing.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_data_converters.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_encodings.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_features.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_headers.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_interface.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_row.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_serialization.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_speed.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/tc_table.rb
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/test_data.csv
/usr/lib64/ruby/gems/2.3.0/gems/fastercsv-1.5.5/test/ts_all.rb
/usr/lib64/ruby/gems/2.3.0/specifications/fastercsv-1.5.5.gemspec
