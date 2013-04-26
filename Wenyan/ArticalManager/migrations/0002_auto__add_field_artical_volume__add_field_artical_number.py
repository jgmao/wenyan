# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Artical.volume'
        db.add_column(u'ArticalManager_artical', 'volume',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Artical.number'
        db.add_column(u'ArticalManager_artical', 'number',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Artical.volume'
        db.delete_column(u'ArticalManager_artical', 'volume')

        # Deleting field 'Artical.number'
        db.delete_column(u'ArticalManager_artical', 'number')


    models = {
        u'ArticalManager.artical': {
            'Meta': {'object_name': 'Artical'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'volume': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['ArticalManager']