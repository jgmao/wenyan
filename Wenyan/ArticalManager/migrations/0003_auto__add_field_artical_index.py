# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artical.index'
        db.add_column(u'ArticalManager_artical', 'index',
                      self.gf('django.db.models.fields.CharField')(default='n/a', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artical.index'
        db.delete_column(u'ArticalManager_artical', 'index')


    models = {
        u'ArticalManager.artical': {
            'Meta': {'object_name': 'Artical'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.CharField', [], {'default': "'n/a'", 'max_length': '200'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['ArticalManager']