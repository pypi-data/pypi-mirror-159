#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : Ampel-ZTF/ampel/ztf/dev/ZTFAlert.py
# License           : BSD-3-Clause
# Author            : vb <vbrinnel@physik.hu-berlin.de>
# Date              : 24.06.2018
# Last Modified Date: 31.07.2020
# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>

import random, fastavro
from ampel.model.UnitModel import UnitModel
from typing import Any, Dict, Optional, List
from ampel.view.LightCurve import LightCurve
from ampel.view.TransientView import TransientView
from ampel.content.DataPoint import DataPoint
from ampel.content.T2Document import T2Document
from ampel.protocol.AmpelAlertProtocol import AmpelAlertProtocol
from ampel.alert.AmpelAlert import AmpelAlert
from ampel.ztf.alert.ZiAlertSupplier import ZiAlertSupplier
from ampel.ztf.ingest.ZiDataPointShaper import ZiDataPointShaperBase


class ZTFAlert:


	@classmethod
	def to_alert(cls, file_path: str) -> AmpelAlert:
		"""
		Creates and returns an instance of ampel.view.LightCurve using a ZTF IPAC alert.
		"""
		als = ZiAlertSupplier(
			deserialize="avro",
			loader=UnitModel(unit="FileAlertLoader", config={"files": [file_path]})
		)

		alert = next(als)
		assert isinstance(alert, AmpelAlert)
		return alert

	@staticmethod
	def _upper_limit_id(el: Dict[str, Any]) -> int:
		return int(
			"%i%s%i" % (
				(2457754.5 - el['jd']) * 1000000,
				str(el['pid'])[8:10],
				round(abs(el['diffmaglim']) * 1000)
			)
		)

	@classmethod
	def to_lightcurve(cls, file_path: Optional[str] = None, pal: Optional[AmpelAlert] = None) -> LightCurve:
		"""
		Creates and returns an instance of ampel.view.LightCurve using a ZTF IPAC alert.
		This is either created from an already existing ampel.alert.PhotoAlert or
		read through a ampel.ztf.alert.ZiAlertSupplier (default).
		In the latter case a path to a stored avro file can be given.
		"""

		if pal is None:
			assert file_path is not None
			pal = cls.to_alert(file_path)
		assert pal is not None

		# convert to DataPoint
		dps = ZiDataPointShaperBase().process(pal.datapoints, pal.stock)

		return LightCurve(
			random.randint(0, (1 << 32) - 1), # CompoundId
			pal.stock,
			tuple(pp for pp in dps if pp["id"] > 0), # Photopoints
			tuple(pp for pp in dps if pp["id"] < 0), # Upperlimit
		)


	# TODO: incomplete/meaningless/quick'n'dirty method, to improve if need be
	@classmethod
	def to_transientview(cls,
		file_path: Optional[str] = None,
		alert: Optional[AmpelAlert] = None,
		content: Optional[Dict] = None,
		t2_docs: Optional[List[T2Document]] = None
	) -> TransientView:
		"""
		Note: incomplete/meaningless//quick'n'dirty method, to improve if need be.
		Creates and returns an instance of ampel.view.LightCurve using a ZTF IPAC alert.
		"""

		if alert is None:
			assert file_path is not None
			alert = cls.to_alert(file_path)
		assert alert is not None
		lc = cls.to_lightcurve(pal=alert)

		datapoints: List[DataPoint] = []
		if lc.photopoints:
			datapoints += list(lc.photopoints)
		if lc.upperlimits:
			datapoints += list(lc.upperlimits)

		return TransientView(
			id = alert.stock,
			t0 = datapoints,
			t2 = t2_docs,
			extra = {
				'names': [alert.extra.get('name') if alert.extra else None]
			}
		)


	@classmethod
	def _load_alert(cls, file_path: str) -> Optional[Dict]:
		""" """
		with open(file_path, 'rb') as f:
			content = cls._deserialize(f)
		return content


	@staticmethod
	def _deserialize(f) -> Optional[Dict]:
		""" """
		reader = fastavro.reader(f)
		return next(reader, None)
