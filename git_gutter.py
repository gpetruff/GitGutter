import sublime, sublime_plugin
import view_collection

class GitGutterCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print 'gutter running'
    self.clear_all()
    # self.lines_removed([10])
    # self.lines_added([5,6,7,8,25,26,27,28,29,30,31,33,34,35,36,37,38])
    # self.lines_modified([39,40,41,46,47,52,53])

    # print git_helper.git_file_path(self.view)
    # view_collection.ViewCollection.add(self.view)
    # gp = view_collection.ViewCollection.git_path(self.view)
    # if gp:
    #   print "git_path: "+gp
    (inserted, modified, deleted) = view_collection.ViewCollection.diff(self.view)
    # if diff:
    #   print "yes diff: "+view_collection.ViewCollection.diff(self.view)
    #   print 'diff end'
    # else:
    #   print 'no diff'
    self.lines_removed(deleted)
    self.lines_added(inserted)
    self.lines_modified(modified)

  def clear_all(self):
    self.view.add_regions('git_gutter_deleted_top',    [], '')
    self.view.add_regions('git_gutter_deleted_bottom', [], '')
    self.view.add_regions('git_gutter_inserted',       [], '')
    self.view.add_regions('git_gutter_changed',        [], '')

  def lines_to_regions(self, lines):
    regions = []
    for line in lines:
      position = self.view.text_point(line-1, 0)
      region   = sublime.Region(position,position)
      regions.append(region)
    return regions

  def lines_removed(self, lines):
    bottom_lines = []
    for line in lines:
      bottom_lines.append(line-1)
    self.lines_removed_top(lines)
    self.lines_removed_bottom(bottom_lines)

  def lines_removed_top(self, lines):
    regions = self.lines_to_regions(lines)
    scope   = "markup.deleted"
    icon    = '../GitGutter/icons/deleted_top'
    self.view.add_regions('git_gutter_deleted_top', regions, scope, icon)

  def lines_removed_bottom(self, lines):
    regions = self.lines_to_regions(lines)
    scope   = "markup.deleted"
    icon    = '../GitGutter/icons/deleted_bottom'
    self.view.add_regions('git_gutter_deleted_bottom', regions, scope, icon)

  def lines_added(self, lines):
    regions = self.lines_to_regions(lines)
    scope   = "markup.inserted"
    icon    = '../GitGutter/icons/inserted'
    self.view.add_regions('git_gutter_inserted', regions, scope, icon)

  def lines_modified(self, lines):
    regions = self.lines_to_regions(lines)
    scope   = "markup.changed"
    icon    = '../GitGutter/icons/changed'
    self.view.add_regions('git_gutter_changed', regions, scope, icon)
